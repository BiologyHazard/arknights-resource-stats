import sys

sys.path.append(".")  # NOQA: E402
from models import ItemInfoList
from scripts.excels import activity_table
from scripts.utils import get_reward_name


def tactical_support():
    item_info_list = ItemInfoList()
    for milestone_group in activity_table["dynActs"]["act1mainlinebp"]["mileStoneGroupMap"].values():
        for bp_data in milestone_group["bpDataList"]:
            reward = bp_data["reward"]
            item_name = get_reward_name(reward)
            item_info_list.append_item_info(item_name, reward["count"])
    return item_info_list


if __name__ == "__main__":
    print(tactical_support())
