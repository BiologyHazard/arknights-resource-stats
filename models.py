from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable, NamedTuple, Self, overload, SupportsIndex

from time_utils import DateTimeLike, to_CST_datetime
from triggers import DateTrigger, Trigger

type ItemInfoLike = ItemInfo | tuple[str, int | float] | str
type ItemInfoListLike = ItemInfoList | Iterable[ItemInfoLike] | str


def _check_tag_name(tag: str) -> None:
    if not tag.startswith("#"):
        raise ValueError(f"Tag should start with '#': {tag!r}")
    if tag.startswith("##"):
        raise ValueError(f"Tag should not start with '##': {tag!r}")


def _check_name(name: str) -> None:
    if name.startswith("#") or name.startswith("!"):
        raise ValueError(f"ResourceItem name should not start with '#' or '!': {name!r}")


REPLACE_DICT = {
    "\\": r"\\",
    "\t": r"\t",
    "\n": r"\n",
    "\r": r"\r",
    "\f": r"\f",
    "\v": r"\v",
    " ": r"\s",
    "×": r"\c",
}


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
        display_name = self.name
        for k, v in REPLACE_DICT.items():
            display_name = display_name.replace(k, v)
        return f"{display_name}×{self.count}"

    @classmethod
    def from_str(cls, s: str) -> Self:
        if "×" not in s:
            return cls(s)
        display_name, amount = s.split("×")
        name = display_name
        for k, v in REPLACE_DICT.items():
            name = name.replace(v, k)
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

    @overload
    def append_item_info(self, item_info: ItemInfoLike, /) -> None:
        ...

    @overload
    def append_item_info(self, item_name: str, item_count: int | float, /) -> None:
        ...

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

    def combine(self) -> Self:
        counter = self.counter()
        return self.__class__(ItemInfo(name, amount) for name, amount in counter.items())

    def combine_in_place(self) -> None:
        counter = self.counter()
        self.clear()
        self.extend(ItemInfo(name, amount) for name, amount in counter.items())

    @classmethod
    def from_str(cls, s: str) -> Self:
        if s == f"{cls.__name__}()":
            return cls()
        return cls(ItemInfo.from_str(item_str) for item_str in s.split())

    @overload
    def __getitem__(self, __i: SupportsIndex) -> ItemInfo:
        ...

    @overload
    def __getitem__(self, __s: slice) -> Self:
        ...

    def __getitem__(self, index: SupportsIndex | slice) -> ItemInfo | Self:
        if isinstance(index, slice):
            return self.__class__(super().__getitem__(index))
        return super().__getitem__(index)

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
    trigger: Trigger

    def __post_init__(self):
        _check_name(self.name)


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
            datetime_or_trigger: DateTimeLike | Trigger,
            *tags: str) -> None:
        if not isinstance(datetime_or_trigger, Trigger):
            datetime_or_trigger = DateTrigger(to_CST_datetime(datetime_or_trigger))
        self.resource_items.append(ResourceItem(ItemInfoList.new(resources), name, datetime_or_trigger))
        if name not in self.tags["##ALL"]:
            self.tags["##ALL"].append(name)
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
        if tag not in self.tags:
            self.tags[tag] = []

    def get_names_by_tag(self,
                         tag_or_name: str,
                         error_if_not_found: bool = True) -> set[str]:
        if not tag_or_name.startswith("#"):
            return {tag_or_name}

        visited: dict[str, set[str]] = {}
        self._search_tag(visited, tag_or_name, error_if_not_found, set())
        return visited[tag_or_name]

    def _search_tag(self,
                    visited: dict[str, set[str]],
                    tag: str,
                    error_if_not_found: bool,
                    recur_visited: set[str]) -> None:
        if error_if_not_found and tag not in self.tags:
            raise ValueError(f"Tag not found: {tag!r}")

        if tag in recur_visited:
            raise ValueError(f"Tag cycle detected: {tag!r}")
        if tag in visited:
            return

        recur_visited.add(tag)
        names: set[str] = set()
        for tag_or_name in self.tags.get(tag, []):  # use get to unnecessary create empty list
            if not tag_or_name.startswith("!"):
                if tag_or_name.startswith("#"):
                    self._search_tag(visited, tag_or_name, error_if_not_found, recur_visited)
                    names.update(visited[tag_or_name])
                else:
                    names.add(tag_or_name)
            else:
                tag_or_name = tag_or_name[1:]
                if tag_or_name.startswith("#"):
                    self._search_tag(visited, tag_or_name, error_if_not_found, recur_visited)
                    names.difference_update(visited[tag_or_name])
                else:
                    names.discard(tag_or_name)
        recur_visited.remove(tag)
        visited[tag] = names

    def tags_to_names(self, tags: list[str] | None = None, error_if_not_found: bool = True) -> dict[str, set[str]]:
        if tags is None:
            _tags: Iterable[str] = self.tags.keys()
        else:
            _tags = tags

        visited: dict[str, set[str]] = {}
        for tag in _tags:
            self._search_tag(visited, tag, error_if_not_found, set())
        return visited

    def get_names_by_filter(self,
                            *tags_or_names: str,
                            error_if_not_found: bool = True) -> set[str]:
        if not tags_or_names or tags_or_names[0].startswith("!"):
            tags_or_names = ("##ALL", *tags_or_names)
        names = set()
        for tag_or_name in tags_or_names:
            if not tag_or_name.startswith("!"):
                names.update(self.get_names_by_tag(tag_or_name, error_if_not_found))
            else:
                names.difference_update(self.get_names_by_tag(tag_or_name[1:], error_if_not_found))
        return names

    def query(self,
              start_time: DateTimeLike,
              end_time: DateTimeLike,
              *tags_or_names: str,
              combine: bool = True,
              error_if_not_found: bool = True) -> ItemInfoList:
        start_time = to_CST_datetime(start_time)
        end_time = to_CST_datetime(end_time)

        names = self.get_names_by_filter(*tags_or_names, error_if_not_found=error_if_not_found)

        result = ItemInfoList()
        for resource_item in self.resource_items:
            if resource_item.name not in names:
                continue
            result.extend(resource_item.resources * len(resource_item.trigger.get_all_fire_time(start_time, end_time)))

        if combine:
            return result.combine()
        else:
            return result

    def advanced_query(self,
                       start_time: DateTimeLike,
                       end_time: DateTimeLike,
                       *tags_or_names: str,
                       error_if_not_found: bool = True) -> defaultdict[str, defaultdict[str, int | float]]:
        start_time = to_CST_datetime(start_time)
        end_time = to_CST_datetime(end_time)

        names = self.get_names_by_filter(*tags_or_names, error_if_not_found=error_if_not_found)
        tags_to_names = self.tags_to_names(None, error_if_not_found)

        result: defaultdict[str, defaultdict[str, int | float]] = defaultdict(lambda: defaultdict(int))
        for resource_item in self.resource_items:
            if resource_item.name not in names:
                continue
            times = len(resource_item.trigger.get_all_fire_time(start_time, end_time))
            if times == 0:
                continue
            for item_info in resource_item.resources:
                result[item_info.name][resource_item.name] += item_info.count * times

        for item_name, item_data in result.items():
            for tag, tag_names in tags_to_names.items():
                value = sum(item_data[name] for name in tag_names if name in item_data)
                if value != 0:
                    item_data[tag] = value

        return result


if __name__ == "__main__":
    rs = ResourceStats()
    rs.add_tag("#A", ["#B"] * 10000, replace=True)
    rs.add_tag("#B", ["#C"] * 10000, replace=True)
    rs.add_tag("#C", ["c", "d", "e"])
    rs.add_tag("#D", ["d", "e", "f"])
    rs.add_tag("#E", ["#A", "#B", "#C", "!#D", "g"])
    print(rs.tags_to_names())
