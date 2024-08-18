from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import NamedTuple, Self, Iterable

from apscheduler.triggers.base import BaseTrigger

CST = timezone(timedelta(hours=8), "中国标准时间")
HG_TIME_DELTA = timedelta(hours=4)
DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

type ItemInfoLike = ItemInfo | tuple[str, int | float] | str
type ItemInfoListLike = ItemInfoList | Iterable[ItemInfoLike] | str


def str_to_CST_datetime(time_str: str, format: str = DEFAULT_TIME_FORMAT) -> datetime:
    return datetime.strptime(time_str, format).replace(tzinfo=CST)


def datetime_to_str(dt: datetime, timezone: timezone | None = None, format: str = DEFAULT_TIME_FORMAT) -> str:
    return dt.astimezone(timezone).strftime(format)


# def get_HG_time(date_str: str):
#     return datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=CST) + HG_TIME_DELTA


def _check_tag_name(tag: str) -> None:
    if not tag.startswith("#"):
        raise ValueError(f"Tag should start with '#': {tag!r}")
    if tag == "#ALL":
        raise ValueError(f"Tag should not be '#ALL'")


class ItemInfo(NamedTuple):
    name: str
    count: int | float = 1

    @classmethod
    def new(cls, arg: ItemInfoLike) -> Self:
        if isinstance(arg, cls):
            return arg
        if isinstance(arg, str):
            return cls.from_str(arg)
        return cls(*arg)

    def __str__(self) -> str:
        return f"{self.name}×{self.count}"

    @classmethod
    def from_str(cls, s: str) -> Self:
        if "×" not in s:
            return cls(s)
        name, amount = s.split("×")
        try:
            return cls(name, int(amount))
        except ValueError:
            return cls(name, float(amount))


class ItemInfoList(list[ItemInfo]):
    @classmethod
    def new(cls, arg: ItemInfoListLike) -> Self:
        if isinstance(arg, cls):
            return arg
        if isinstance(arg, str):
            return cls.from_str(arg)
        return cls(ItemInfo.new(item) for item in arg)

    def append_item_info(self, *args) -> None:
        if len(args) == 1:
            arg, = args
            self.append(ItemInfo.new(arg))
        else:
            self.append(ItemInfo.new(args))

    def counter(self) -> defaultdict[str, int | float]:
        counter: defaultdict[str, int | float] = defaultdict(int)
        for item in self:
            counter[item.name] += item.count
        return counter

    def combine(self) -> list[ItemInfo]:
        counter = self.counter()
        return [ItemInfo(name, amount) for name, amount in counter.items()]

    def combine_in_place(self) -> None:
        counter = self.counter()
        self.clear()
        self.extend(ItemInfo(name, amount) for name, amount in counter.items())

    @classmethod
    def from_str(cls, s: str) -> Self:
        return cls(ItemInfo.from_str(item_str) for item_str in s.split())

    def __str__(self) -> str:
        if not self:
            return f"{self.__class__.__name__}()"
        return " ".join(map(str, self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class ResourceItem:
    resources: ItemInfoList
    name: str
    trigger: BaseTrigger

    def __post_init__(self):
        if self.name.startswith("#") or self.name.startswith("!"):
            raise ValueError(f"ResourceItem name should not start with '#' or '!': {self.name!r}")


class ResourceStats:
    def __init__(self, resource_items: list[ResourceItem] | None = None, tags: dict[str, list[str]] | None = None):
        if resource_items is None:
            resource_items = []
        if tags is None:
            tags = defaultdict(list)
        else:
            tags = defaultdict(list, tags)

        self.resource_items: list[ResourceItem] = resource_items
        self.tags: defaultdict[str, list[str]] = tags

    def add(self,
            resources: ItemInfoListLike,
            name: str,
            trigger: BaseTrigger,
            *tags: str) -> None:
        self.resource_items.append(ResourceItem(ItemInfoList.new(resources), name, trigger))
        if name not in self.tags["#ALL"]:
            self.tags["#ALL"].append(name)
        for tag in tags:
            _check_tag_name(tag)
            if name not in self.tags[tag]:
                self.tags[tag].append(name)

    def add_tag(self, tag: str, tags_or_names: list[str], replace: bool = False) -> None:
        _check_tag_name(tag)
        if replace:
            self.tags[tag] = tags_or_names
        else:
            for tag_or_name in tags_or_names:
                if tag_or_name not in self.tags[tag]:
                    self.tags[tag].append(tag_or_name)

    def get_names_by_tag(self,
                         tag: str,
                         error_if_not_found: bool = True,
                         visited: set[str] | None = None,
                         recur_visited: set[str] | None = None) -> set[str]:
        if not tag.startswith("#"):  # param 'tag' is actually a name
            return {tag}

        if error_if_not_found and tag not in self.tags:
            raise ValueError(f"Tag not found: {tag!r}")

        if visited is None:
            visited = set()
        if recur_visited is None:
            recur_visited = set()

        if tag in recur_visited:
            raise ValueError(f"Tag cycle detected: {tag!r}")
        if tag in visited:
            return set()

        visited.add(tag)
        recur_visited.add(tag)
        names = set()
        for tag_or_name in self.tags[tag]:
            if tag_or_name.startswith("#"):
                names.update(self.get_names_by_tag(tag_or_name, error_if_not_found, visited, recur_visited))
            else:
                names.add(tag_or_name)
        recur_visited.remove(tag)

        return names

    def get_names_by_filter(self,
                            *tags_or_names: str,
                            error_if_not_found: bool = True) -> set[str]:
        if not tags_or_names or tags_or_names[0].startswith("!"):
            tags_or_names = ("#ALL", ) + tags_or_names
        names = set()
        for tag_or_name in tags_or_names:
            if not tag_or_name.startswith("!"):
                names.update(self.get_names_by_tag(tag_or_name, error_if_not_found))
            else:
                names.difference_update(self.get_names_by_tag(tag_or_name[1:], error_if_not_found))
        return names

    def query(self,
              start_time: datetime | str,
              end_time: datetime | str,
              *tags_or_names: str,
              combine: bool = True,
              error_if_not_found: bool = True) -> list[ItemInfo]:
        if isinstance(start_time, str):
            start_time = str_to_CST_datetime(start_time)
        if isinstance(end_time, str):
            end_time = str_to_CST_datetime(end_time)

        names = self.get_names_by_filter(*tags_or_names, error_if_not_found=error_if_not_found)

        result = ItemInfoList()
        for resource_item in self.resource_items:
            if resource_item.name not in names:
                continue
            trigger: BaseTrigger = resource_item.trigger
            next_fire_time = trigger.get_next_fire_time(None, start_time)
            while next_fire_time is not None and next_fire_time < end_time:
                result.extend(resource_item.resources)
                next_fire_time = trigger.get_next_fire_time(next_fire_time, next_fire_time)

        if combine:
            return result.combine()
        else:
            return result


if __name__ == "__main__":
    # rs = ResourceStats()
    # rs.tags = defaultdict(list, {
    #     "#ALL": ["#A", "#B"] * 10000,
    #     "#A": ["#B", "#B"] * 10000,
    #     "#B": ["#C", "a", "e"],
    #     "#C": ["d", "e"],
    # })

    # print(rs.get_names_by_tag("#ALL"))
    # print(repr(ItemInfoList("龙门币")))
    print(repr(ItemInfoList.new(ItemInfoList.new("龙门币"))))
