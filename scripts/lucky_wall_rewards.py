from collections.abc import Generator
from datetime import timedelta
from textwrap import dedent

from models import ItemInfoList
from scripts.excels import activity_table
from scripts.manager import Line, manager
from scripts.utils import get_event_name
from time_utils import to_CST_datetime, to_CST_time_str


@manager.register(
    file_name="lucky_wall",
    function_name="add_lucky_wall_resources",
    import_str="""from models import ResourceStats
from time_utils import CST
from triggers import DateTrigger, CronTrigger

from .manager import manager""",
)
def lucky_wall_rewards() -> Generator[Line, None, None]:
    for event_id, event_basic_info in activity_table["basicInfo"].items():
        if event_basic_info["type"] == "PRAY_ONLY":
            event_start_timestamp = event_basic_info["startTime"]
            event_start_datetime = to_CST_datetime(event_start_timestamp)
            event_name = get_event_name(event_id)
            item_info_list = ItemInfoList.new([("合成玉", 8304.13/14)])
            date_str = to_CST_time_str(event_start_datetime.replace(hour=16))
            start_time_str = to_CST_time_str(event_start_datetime.replace(hour=4) + timedelta(days=1))
            end_time_str = to_CST_time_str(event_start_datetime.replace(hour=4) + timedelta(days=14))
            trigger_str = dedent(f"""
                DateTrigger({date_str!r})
                | CronTrigger(hour=4, start_time={start_time_str!r}, end_time={end_time_str!r}, timezone=CST)
                """).strip("\n")

            yield item_info_list, event_name, trigger_str, ["#幸运墙活动"], 6
