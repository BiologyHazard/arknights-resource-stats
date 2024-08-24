import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.excels import activity_table
from scripts.utils import get_reward_name, Reward


def reclamation_algorithm_mission():
    item_info_list = ItemInfoList()
    for collection in activity_table["activity"]["COLLECTION"]["act1collection"]["collections"]:
        reward = Reward(type=collection["itemType"],
                        id=collection["itemId"],
                        count=collection["itemCnt"])
        item_name = get_reward_name(reward)
        item_info_list.append_item_info(item_name, collection["itemCnt"])
    return item_info_list


if __name__ == "__main__":
    print(reclamation_algorithm_mission())
