import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.utils import get_reward_item_info_list
from scripts.excels import activity_table


def design_of_strife():
    item_info_list = ItemInfoList()
    for milestone in activity_table["activity"]["TYPE_ACT42D0"]["act42d0"]["milestoneData"]:
        reward = milestone["item"]
        item_info_list.extend(get_reward_item_info_list(reward))
    return item_info_list


if __name__ == "__main__":
    print(design_of_strife())
