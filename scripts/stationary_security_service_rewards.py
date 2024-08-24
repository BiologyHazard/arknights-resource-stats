from collections.abc import Generator

from models import ItemInfoList
from scripts.excels import climb_tower_table
from scripts.manager import Line, manager
from scripts.utils import get_reward_name


@manager.register(
    file_name="stationary_security_service",
    function_name="add_stationary_security_service_resources",
    import_str="""from models import ResourceStats

from .manager import manager""",
)
def stationary_security_service_rewards() -> Generator[Line, None, None]:
    for season_id, season_data in climb_tower_table["seasonInfos"].items():
        season_name = season_data["name"]
        season_start_timestamp = season_data["startTs"]
        for tower_id in season_data["towers"]:
            tower_data = climb_tower_table["towers"][tower_id]
            tower_name = tower_data["name"]
            item_info_list = ItemInfoList()
            for task_info in tower_data["taskInfo"]:
                for reward in task_info["rewards"]:
                    item_info_list.append_item_info(get_reward_name(reward), reward["count"])
            yield item_info_list, f"{tower_name}首次清理记录", season_start_timestamp, ["#保全派驻首次清理记录"], 6

    for season_id, mission_group in climb_tower_table["missionGroup"].items():
        season_data = climb_tower_table["seasonInfos"][season_id]
        season_name = season_data["name"]
        season_start_timestamp = season_data["startTs"]
        item_info_list = ItemInfoList()
        assert not mission_group["rewards"]
        for mission_id in mission_group["missionIds"]:
            mission_data = climb_tower_table["missionData"][mission_id]
            for reward in mission_data["rewards"]:
                item_info_list.append_item_info(get_reward_name(reward), reward["count"])
        yield item_info_list, f"{season_name}任务", season_start_timestamp, ["#保全派驻任务"], 6
