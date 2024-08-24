import sys
from collections.abc import Iterable
from datetime import datetime
from textwrap import indent as textwrap_indent
from typing import Literal

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.annihilation_rewards import *
from scripts.check_in_rewards import *
from scripts.event_mission_rewards import *
from scripts.integrated_strategies_rewards import *
from scripts.login_rewards import *
from scripts.lucky_wall_rewards import *
from scripts.manager import Line, manager
from scripts.stationary_security_service_rewards import *
from scripts.trials_for_navigator_rewards import *
from scripts.zone_record_rewards import *
from time_utils import DateTimeLike, to_CST_datetime, to_CST_time_str


def generate_line(item_info_list: ItemInfoList,
                  name: str,
                  start_time_or_trigger_str: DateTimeLike | str,
                  tags: list[str],
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
{textwrap_indent(start_time_or_trigger_str, " " * 4)},
    {tags_str},
)
""".strip('\n')
    return code


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

        # == code start ==
        code = f"""{import_str.strip()}


@manager.register
def {function_name}(resource_stats: ResourceStats):
{comments}{textwrap_indent(generate_lines(function()), " " * 4)}
"""
        # == code end ==

        with open(f"rewards/{file_name}.py", "w", encoding="utf-8") as f:
            f.write(code)


if __name__ == "__main__":
    generate_code()
