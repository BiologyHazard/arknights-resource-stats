from collections.abc import Generator
from datetime import timedelta

from models import ItemInfoList
from scripts.excels import activity_table
from scripts.manager import Line, manager
from scripts.utils import get_event_name, get_reward_item_info_list
from time_utils import to_CST_datetime

numbers = "〇 一 二 三 四 五 六 七 八 九 十 十一 十二 十三 十四 十五 十六 十七 十八 十九 二十 二十一 二十二 二十三 二十四 二十五 二十六 二十七 二十八 二十九 三十 三十一 三十二 三十三 三十四 三十五 三十六 三十七 三十八 三十九 四十 四十一 四十二 四十三 四十四 四十五 四十六 四十七 四十八 四十九 五十".split()


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
                item_info_list.extend(get_reward_item_info_list(reward))

            yield item_info_list, f"{event_name}第{numbers[day+1]}日", time, [f"#{event_name}", "#常规签到活动"], 2

        for extra_check_in_list in event_data["extraCheckinList"] or []:
            timestamp = extra_check_in_list["absolutData"]

            item_info_list = ItemInfoList()
            for reward in extra_check_in_list["itemList"]:
                item_info_list.extend(get_reward_item_info_list(reward))

            yield item_info_list, f"{event_name}额外", timestamp, [f"#{event_name}", "#常规签到活动"], 2
