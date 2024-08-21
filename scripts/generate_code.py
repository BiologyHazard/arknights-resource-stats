import sys
from collections.abc import Iterable
from datetime import datetime
from textwrap import dedent
from textwrap import indent as textwrap_indent
from typing import Literal

sys.path.append(r".")
from models import ItemInfoList  # NOQA: E402
from scripts.annihilation_rewards import annihilation_rewards  # NOQA: E402
from scripts.event_mission_rewards import (checkin_only_rewards, event_mission_rewards,  # NOQA: E402
                                           login_only_rewards, pray_only_rewards)
from scripts.integrated_strategies_rewards import integrated_strategies_rewards  # NOQA: E402
from scripts.manager import FunctionInfo, Line, manager  # NOQA: E402
from scripts.trials_for_navigator_rewards import trials_for_navigator_rewards  # NOQA: E402
from scripts.zone_record_rewards import zone_record_rewards  # NOQA: E402
from time_utils import DateTimeLike, to_CST_datetime, to_CST_time_str  # NOQA: E402


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
    try:
        _ = to_CST_datetime(start_time_or_trigger_str)
    except Exception:
        pass
    else:
        start_time_or_trigger_str = repr(start_time_or_trigger_str)
    tags_str = ", ".join(repr(tag) for tag in tags)

    if lines == 1:
        code = f"resource_stats.add({item_info_list_str}, {name_str}, {start_time_or_trigger_str}, {tags_str})"
    elif lines == 2:
        code = f"resource_stats.add({item_info_list_str},\n{" " * 19}{name_str}, {start_time_or_trigger_str}, {tags_str})"
    else:
        code = f"""
resource_stats.add(
    {item_info_list_str},
    {name_str},
{textwrap_indent(start_time_or_trigger_str, "    ")},
    {tags_str},
)
""".strip('\n')
    return textwrap_indent(code, " " * indent)


def generate_lines(
    arg: Iterable[Line],
    join_str: str = "\n",
) -> str:
    lines = [generate_line(*element) for element in arg]
    return join_str.join(lines)


def generate_code():
    for function, file_name, function_name, import_str, comments in manager:
        if comments:
            comments = f"    {comments}\n"
        code = f"""{import_str.strip()}


def {function_name}(resource_stats: ResourceStats):
{comments}{generate_lines(function())}
"""
        with open(f"rewards/{file_name}.py", "w", encoding="utf-8") as f:
            f.write(code)


if __name__ == "__main__":
    generate_code()
