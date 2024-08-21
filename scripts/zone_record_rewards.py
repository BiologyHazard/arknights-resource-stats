from collections.abc import Generator

from models import ItemInfoList
from scripts.excels import zone_table
from scripts.manager import Line, manager
from scripts.utils import get_reward_name


@manager.register(
    file_name="zone_record",
    function_name="add_zone_record_resources",
    import_str="from models import ResourceStats",
)
def zone_record_rewards() -> Generator[Line, None, None]:
    for zone_id, zone_data in zone_table["zoneRecordGroupedData"].items():
        zone_name_first = zone_table["zones"][zone_id]["zoneNameFirst"]
        zone_name_second = zone_table["zones"][zone_id]["zoneNameSecond"]
        zone_name = f"{zone_name_first}{zone_name_second}"
        initial_name = zone_data["unlockData"]["initialName"]
        resource_name = f"{zone_name} - {initial_name}"
        zone_open_time = zone_table["mainlineAdditionInfo"][zone_id]["zoneOpenTime"]

        item_info_list = ItemInfoList()
        for record in zone_data["records"]:
            for reward_data in record["rewards"]:
                for reward in reward_data["recordReward"] or []:
                    reward_name = get_reward_name(reward)
                    item_info_list.append_item_info(reward_name, reward["count"])
        yield item_info_list, resource_name, zone_open_time, [f"#{zone_name}", "#主题曲记录点奖励"], 4, 6
