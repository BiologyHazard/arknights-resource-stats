import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.excels import activity_table
from scripts.utils import Reward, get_reward_item_info_list


def reclamation_algorithm_mission():
    item_info_list = ItemInfoList()
    for collection in activity_table["activity"]["COLLECTION"]["act1collection"]["collections"]:
        reward = Reward(type=collection["itemType"],
                        id=collection["itemId"],
                        count=collection["itemCnt"])
        item_info_list.extend(get_reward_item_info_list(reward))
    return item_info_list


if __name__ == "__main__":
    print(reclamation_algorithm_mission())
