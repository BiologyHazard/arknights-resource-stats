from collections.abc import Generator

from models import ItemInfoList
from scripts.excels import activity_table
from scripts.manager import Line, manager
from scripts.utils import furniture_to_intelligence_certificate, get_event_name, get_reward_name, get_reward_type


@manager.register(
    file_name="event_mission",
    function_name="add_event_mission_resources",
    import_str="""from models import ResourceStats

from .manager import manager""",
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

        yield item_info_list, f"{event_name}任务", event_start_timestamp, [f"#{event_name}", "#活动任务"], 6
