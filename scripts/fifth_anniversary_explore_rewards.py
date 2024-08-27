import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.excels import activity_table
from scripts.utils import get_reward_item_info_list


def fifth_anniversary_explore_rewards():
    item_info_list = ItemInfoList()
    for mission_data in activity_table["fifthAnnivExploreData"]["missionData"].values():
        for reward in mission_data["rewards"]:
            item_info_list.extend(get_reward_item_info_list(reward))
    return item_info_list


if __name__ == "__main__":
    item_info_list = fifth_anniversary_explore_rewards()
    print(item_info_list)
