from collections.abc import Generator
from datetime import timedelta
from textwrap import dedent

from models import ItemInfoList
from scripts.excels import activity_table
from scripts.manager import Line, manager
from scripts.utils import furniture_to_intelligence_certificate, get_event_name, get_reward_name, get_reward_type
from time_utils import to_CST_datetime, to_CST_time_str


@manager.register(
    file_name="event_mission",
    function_name="add_event_mission_resources",
    import_str="from models import ResourceStats",
)
def event_mission_rewards() -> Generator[Line, None, None]:
    mission_data_dict = {mission_data["id"]: mission_data for mission_data in activity_table["missionData"]}

    for mission_group in activity_table["missionGroup"]:
        assert mission_group["title"] is None
        assert mission_group["type"] == "ACTIVITY"
        assert mission_group["preMissionGroup"] is None
        assert mission_group["period"] is None

        event_id = mission_group["id"]
        event_basic_info = activity_table["basicInfo"][event_id]
        event_name = get_event_name(event_id)
        event_start_timestamp = event_basic_info["startTime"]
        is_replicate = event_basic_info["isReplicate"]

        item_info_list = ItemInfoList()
        for reward in mission_group["rewards"] or []:
            item_name = get_reward_name(reward)
            item_info_list.append_item_info(item_name, reward["count"])

        for mission_id in mission_group["missionIds"]:
            mission_data = mission_data_dict[mission_id]
            for reward in mission_data["rewards"] or []:
                if reward["count"] == 0:  # "23sreActivity_1" 的 "“鼓声争鸣”" 等的数量为 0
                    continue
                if not is_replicate or get_reward_type(reward) != "FURN":
                    item_name = get_reward_name(reward)
                    item_info_list.append_item_info(item_name, reward["count"])
                else:  # 复刻活动的家具奖励
                    intelligence_certificate_count = furniture_to_intelligence_certificate(event_id, reward["id"]) * reward["count"]
                    item_info_list.append_item_info("情报凭证", intelligence_certificate_count)

        yield item_info_list, f"{event_name}任务", event_start_timestamp, [f"#{event_name}", "#活动任务"], 4, 6


@manager.register(
    file_name="login",
    function_name="add_login_resources",
    import_str="from models import ResourceStats",
)
def login_only_rewards() -> Generator[Line, None, None]:
    assert ([event_id
             for event_id, event_basic_info in activity_table["basicInfo"].items()
             if event_basic_info["type"] == "LOGIN_ONLY"]
            == list(activity_table["activity"]["LOGIN_ONLY"]))
    for event_id in activity_table["activity"]["LOGIN_ONLY"]:
        event_basic_info = activity_table["basicInfo"][event_id]
        event_data = activity_table["activity"]["LOGIN_ONLY"][event_id]
        event_start_timestamp = event_basic_info["startTime"]
        event_name = get_event_name(event_id)

        item_info_list = ItemInfoList()
        for reward in event_data["itemList"]:
            item_name = get_reward_name(reward)
            item_info_list.append_item_info(item_name, reward["count"])

        yield item_info_list, event_name, event_start_timestamp, ["#登录活动"], 4, 6


@manager.register(
    file_name="check_in",
    function_name="add_check_in_resources",
    import_str="from models import ResourceStats",
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

            yield item_info_list, event_name, time, ["#签到活动"], 4, 2

        for extra_check_in_list in event_data["extraCheckinList"] or []:
            timestamp = extra_check_in_list["absolutData"]

            item_info_list = ItemInfoList()
            for reward in extra_check_in_list["itemList"]:
                item_name = get_reward_name(reward)
                item_info_list.append_item_info(item_name, reward["count"])

            yield item_info_list, event_name, timestamp, ["#签到活动"], 4, 2


@manager.register(
    file_name="lucky_wall",
    function_name="add_lucky_wall_resources",
    import_str="""from models import ResourceStats
from time_utils import CST
from triggers import DateTrigger, CronTrigger""",
)
def pray_only_rewards() -> Generator[Line, None, None]:
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

            yield item_info_list, event_name, trigger_str, ["#幸运墙活动"], 4, 6
