import sys
from collections.abc import Generator

sys.path.append(r".")
from models import ItemInfo, ItemInfoList  # NOQA: E402
from scripts.excels import activity_table, item_table, skin_table  # NOQA: E402
from scripts.manager import Line, manager  # NOQA: E402


@manager.register
def trails_for_navigator_rewards() -> Generator[Line, None, None]:
    # tfn for "trials for navigator"
    for tfn_id, tfn_info in activity_table["activity"]["BOSS_RUSH"].items():
        basic_info = activity_table["basicInfo"][tfn_id]
        tfn_index = tfn_id.lstrip("act").rstrip("bossrush")
        tfn_index = f"{int(tfn_index):02d}"
        tfn_name = f"{basic_info["name"]}#{tfn_index}"
        tfn_start_timestamp = basic_info["startTime"]

        mile_stone_list = tfn_info["mileStoneList"]
        need_point_count = mile_stone_list[-1]["needPointCnt"]

        item_info_list = ItemInfoList([ItemInfo("试炼经验", -need_point_count)])
        for mile_stone in mile_stone_list:
            reward_item = mile_stone["rewardItem"]
            item_id = reward_item["id"]
            item_count = reward_item["count"]
            item_type = reward_item["type"]
            if item_type == "CHAR_SKIN":
                item_name = skin_table["charSkins"][item_id]["displaySkin"]["skinName"]
            else:
                item_name = item_table["items"][item_id]["name"]
            item_info_list.append_item_info(item_name, item_count)

        yield item_info_list, f"{tfn_name}试炼之路", tfn_start_timestamp, [f"#{tfn_name}", "#引航者试炼"], 4, 6
