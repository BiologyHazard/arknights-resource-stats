import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.utils import get_reward_name, Reward
from scripts.excels import activity_table


def siestan_fashion_street():
    item_info_list = ItemInfoList()
    for milestone in activity_table["activity"]["TYPE_ACT27SIDE"]["act27side"]["mileStoneList"]:
        reward = milestone["rewardItem"]
        item_name = get_reward_name(reward)
        item_info_list.append_item_info(item_name, reward["count"])
    return item_info_list


if __name__ == "__main__":
    print(siestan_fashion_street())
