import sys
from datetime import datetime
from textwrap import dedent
from textwrap import indent as textwrap_indent
from typing import Iterable, Literal

sys.path.append(r".")
from models import ItemInfoList  # NOQA: E402
from time_utils import DateTimeLike, to_CST_time_str  # NOQA: E402


class Manager(list):
    def register(self, func):
        self.append(func)
        return func


manager = Manager()


def generate_line(item_info_list: ItemInfoList,
                  name: str,
                  start_time_or_trigger_str: DateTimeLike | str,
                  tags: list[str],
                  indent: int,
                  lines: Literal[1, 2, 6]) -> str:
    item_info_list_str = repr(str(item_info_list))
    name_str = repr(name)
    if isinstance(start_time_or_trigger_str, datetime | int | float):
        start_time_or_trigger_str = to_CST_time_str(start_time_or_trigger_str)
    start_time_or_trigger_str = repr(start_time_or_trigger_str)
    tags_str = ", ".join(repr(tag) for tag in tags)

    if lines == 1:
        code = f"resource_stats.add({item_info_list_str}, {name_str}, {start_time_or_trigger_str}, {tags_str})"
    elif lines == 2:
        code = f"resource_stats.add({item_info_list_str},\n{" " * 19}{name_str}, {start_time_or_trigger_str}, {tags_str})"
    else:
        code = dedent(f"""
            resource_stats.add(
                {item_info_list_str},
                {name_str},
            {textwrap_indent(start_time_or_trigger_str, "    ")},
                {tags_str},
            )
            """).strip('\n')
    return textwrap_indent(code, " " * indent)


def generate_lines(
    arg: Iterable[tuple[ItemInfoList, str, DateTimeLike | str, list[str], int, Literal[1, 2, 6]]],
    join_str: str = "\n",
) -> str:
    lines = [generate_line(*element) for element in arg]
    return join_str.join(lines)


@manager.register
def add(*args, **kwargs):
    return generate_line(*args, **kwargs)


print(manager)
