from collections.abc import Generator
from datetime import timedelta

from models import ItemInfoList
from scripts.excels import activity_table
from scripts.manager import Line, manager
from scripts.utils import get_event_name, get_reward_name
from time_utils import to_CST_datetime


@manager.register(
    file_name="check_in",
    function_name="add_check_in_resources",
    import_str="""from models import ResourceStats

from .manager import manager""",
)
def checkin_only_rewards() -> Generator[Line, None, None]:
    assert ([event_id
             for event_id, event_basic_info in activity_table["basicInfo"].items()
             if event_basic_info["type"] == "CHECKIN_ONLY"]
            == list(activity_table["activity"]["CHECKIN_ONLY"]))
    for event_id in activity_table["activity"]["CHECKIN_ONLY"]:
        event_basic_info = activity_table["basicInfo"][event_id]
        event_data = activity_table["activity"]["CHECKIN_ONLY"][event_id]
        event_start_timestamp = event_basic_info["startTime"]
        event_start_time = to_CST_datetime(event_start_timestamp)
        event_name = get_event_name(event_id)

        for day_str, check_in_list in event_data["checkInList"].items():
            day = int(day_str)
            assert check_in_list["order"] == day + 1
            time = event_start_time + timedelta(days=day)
            if day > 0:
                time = time.replace(hour=4)

            item_info_list = ItemInfoList()
            for reward in check_in_list["itemList"]:
                item_name = get_reward_name(reward)
                item_info_list.append_item_info(item_name, reward["count"])

            yield item_info_list, event_name, time, ["#签到活动"], 2

        for extra_check_in_list in event_data["extraCheckinList"] or []:
            timestamp = extra_check_in_list["absolutData"]

            item_info_list = ItemInfoList()
            for reward in extra_check_in_list["itemList"]:
                item_name = get_reward_name(reward)
                item_info_list.append_item_info(item_name, reward["count"])

            yield item_info_list, event_name, timestamp, ["#签到活动"], 2
