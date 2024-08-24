import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfo, ItemInfoList
from scripts.event_start_time import event_start_time
from scripts.utils import furniture_to_intelligence_certificate, get_event_id_by_name, get_furniture_id_by_name, get_reward_name
from scripts.excels import activity_table


def fifth_anniversary_explore_rewards():
    item_info_list = ItemInfoList()
    for mission_data in activity_table["fifthAnnivExploreData"]["missionData"].values():
        for reward in mission_data["rewards"]:
            item_name = get_reward_name(reward)
            item_info_list.append_item_info(item_name, reward["count"])
    return item_info_list


if __name__ == "__main__":
    item_info_list = fifth_anniversary_explore_rewards()
    print(item_info_list)
