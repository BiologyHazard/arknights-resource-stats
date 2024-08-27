import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.excels import activity_table
from scripts.utils import get_reward_item_info_list


def tactical_support():
    item_info_list = ItemInfoList()
    for milestone_group in activity_table["dynActs"]["act1mainlinebp"]["mileStoneGroupMap"].values():
        for bp_data in milestone_group["bpDataList"]:
            reward = bp_data["reward"]
            item_info_list.extend(get_reward_item_info_list(reward))
    return item_info_list


if __name__ == "__main__":
    print(tactical_support())
