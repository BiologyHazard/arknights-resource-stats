import sys
from datetime import timedelta
from textwrap import dedent

sys.path.append(r".")
from models import ItemInfoList  # NOQA: E402
from scripts.excels import activity_table, replicate_table  # NOQA: E402
from scripts.generate_code import generate_line  # NOQA: E402
from scripts.utils import (furniture_to_intelligence_certificate,  # NOQA: E402
                           get_event_name, get_reward_name, get_reward_type)
from time_utils import get_CST_datetime, get_CST_time_str  # NOQA: E402


def event_mission_rewards():
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

        print(generate_line(item_info_list, f"{event_name}任务", event_start_timestamp, ["#活动任务"], 4, 6))


def login_only_rewards():
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

        print(generate_line(item_info_list, event_name, event_start_timestamp, ["#登录活动"], 4, 6))


def checkin_only_rewards():
    assert ([event_id
             for event_id, event_basic_info in activity_table["basicInfo"].items()
             if event_basic_info["type"] == "CHECKIN_ONLY"]
            == list(activity_table["activity"]["CHECKIN_ONLY"]))
    for event_id in activity_table["activity"]["CHECKIN_ONLY"]:
        event_basic_info = activity_table["basicInfo"][event_id]
        event_data = activity_table["activity"]["CHECKIN_ONLY"][event_id]
        event_start_timestamp = event_basic_info["startTime"]
        event_start_time = get_CST_datetime(event_start_timestamp)
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

            print(generate_line(item_info_list, event_name, time, ["#签到活动"], 4, 2))

        for extra_check_in_list in event_data["extraCheckinList"] or []:
            timestamp = extra_check_in_list["absolutData"]

            item_info_list = ItemInfoList()
            for reward in extra_check_in_list["itemList"]:
                item_name = get_reward_name(reward)
                item_info_list.append_item_info(item_name, reward["count"])

            print(generate_line(item_info_list, event_name, timestamp, ["#签到活动"], 4, 2))


def pray_only_rewards():
    for event_id, event_basic_info in activity_table["basicInfo"].items():
        if event_basic_info["type"] == "PRAY_ONLY":
            event_start_timestamp = event_basic_info["startTime"]
            event_start_datetime = get_CST_datetime(event_start_timestamp)
            event_name = get_event_name(event_id)
            item_info_list = ItemInfoList.new([("合成玉", 8304.13/14)])
            date_str = get_CST_time_str(event_start_datetime.replace(hour=16))
            start_date_str = get_CST_time_str(event_start_datetime.replace(hour=4) + timedelta(days=1))
            end_date_str = get_CST_time_str(event_start_datetime.replace(hour=4) + timedelta(days=14))
            trigger_str = dedent(f"""
                OrTrigger([
                    DateTrigger({date_str!r}, timezone=CST),
                    CronTrigger(hour=4, start_date={start_date_str!r}, end_date={end_date_str!r}, timezone=CST),
                ])
                """).strip("\n")

            print(generate_line(item_info_list, event_name, trigger_str, ["#幸运墙活动"], 4, 6))


if __name__ == "__main__":
    event_mission_rewards()
    # login_only_rewards()
    # checkin_only_rewards()
    # pray_only_rewards()
