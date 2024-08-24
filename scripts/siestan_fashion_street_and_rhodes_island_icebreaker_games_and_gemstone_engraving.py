import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.excels import activity_table
from scripts.utils import get_reward_name


def siestan_fashion_street():
    item_info_list = ItemInfoList()
    for milestone in activity_table["activity"]["TYPE_ACT27SIDE"]["act27side"]["mileStoneList"]:
        reward = milestone["rewardItem"]
        item_name = get_reward_name(reward)
        item_info_list.append_item_info(item_name, reward["count"])
    return item_info_list


def rhodes_island_icebreaker_games():
    item_info_list = ItemInfoList()
    for milestone in activity_table["activity"]["MULTIPLAY_VERIFY2"]["act2vmulti"]["mileStoneList"]:
        reward = milestone["rewardItem"]
        item_name = get_reward_name(reward)
        item_info_list.append_item_info(item_name, reward["count"])
    return item_info_list


def gemstone_engraving():
    item_info_list = ItemInfoList()
    for milestone in activity_table["activity"]["TYPE_ACT35SIDE"]["act35side"]["mileStoneList"]:
        reward = milestone["rewardItem"]
        item_name = get_reward_name(reward)
        item_info_list.append_item_info(item_name, reward["count"])
    return item_info_list


def siestan_fashion_street_replicate():
    item_info_list = ItemInfoList()
    for milestone in activity_table["activity"]["TYPE_ACT27SIDE"]["act27sre"]["mileStoneList"]:
        reward = milestone["rewardItem"]
        item_name = get_reward_name(reward)
        item_info_list.append_item_info(item_name, reward["count"])
    return item_info_list


if __name__ == "__main__":
    # print(siestan_fashion_street())
    # print(rhodes_island_icebreaker_games())
    # print(gemstone_engraving())
    print(siestan_fashion_street_replicate())
