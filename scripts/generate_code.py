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
from scripts.manager import FunctionInfo, Line, manager  # NOQA: E402
from scripts.trials_for_navigator_rewards import trials_for_navigator_rewards  # NOQA: E402
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
#     start = """
# from models import ResourceStats
# from time_utils import CST
# from triggers import CronTrigger, DateTrigger


# def add_generated_resources(resource_stats: ResourceStats):
# """.lstrip()

#     with open("rewards/annihilation.py", "w", encoding="utf-8") as f:
#         start = '''
# from models import ResourceStats


# def add_annihilation_first_clear_resources(resource_stats: ResourceStats):
#     """不计理智消耗，不计合成玉报酬"""
# '''.lstrip()
#         f.write(start)
#         f.write(generate_lines(annihilation_rewards()))

#     with open("rewards/check_in.py", "w", encoding="utf-8") as f:
#         start = '''
# from models import ResourceStats


# def add_check_in_resources(resource_stats: ResourceStats):
# '''.lstrip()
#         f.write(start)
#         f.write(generate_lines(checkin_only_rewards()))

#     with open("rewards/event_mission.py", "w", encoding="utf-8") as f:
#         start = '''
# from models import ResourceStats


# def add_event_mission_resources(resource_stats: ResourceStats):
# '''.lstrip()
#         f.write(start)
#         f.write(generate_lines(event_mission_rewards()))

#     with open("rewards/login.py", "w", encoding="utf-8") as f:
#         start = '''
# from models import ResourceStats


# def add_login_resources(resource_stats: ResourceStats):
# '''.lstrip()
#         f.write(start)
#         f.write(generate_lines(login_only_rewards()))

#     with open("rewards/lucky_wall.py", "w", encoding="utf-8") as f:
#         start = '''
# from models import ResourceStats
# from time_utils import CST
# from triggers import DateTrigger, CronTrigger


# def add_lucky_wall_resources(resource_stats: ResourceStats):
# '''.lstrip()
#         f.write(start)
#         f.write(generate_lines(pray_only_rewards()))

#     with open("rewards/trials_for_navigator.py", "w", encoding="utf-8") as f:
#         start = '''
# from models import ResourceStats


# def add_trials_for_navigator_resources(resource_stats: ResourceStats):
# '''.lstrip()
#         f.write(start)
#         f.write(generate_lines(trails_for_navigator_rewards()))
