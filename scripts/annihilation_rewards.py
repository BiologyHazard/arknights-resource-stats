import sys
from datetime import datetime

sys.path.append(r".")
from models import ItemInfoList  # NOQA: E402
from scripts.excels import building_data, campaign_table, item_table, stage_table  # NOQA: E402
from scripts.generate_code import generate_line  # NOQA: E402

campaign_rewards = []
for campaign in campaign_table["campaigns"].values():
    campaign_name = stage_table["stages"][campaign["stageId"]]["name"]
    # campaign start time
    if campaign_name in ("切尔诺伯格", "龙门外环"):
        campaign_start_time = datetime(2019, 4, 30, 10)
    elif campaign_name == "龙门市区":
        campaign_start_time = datetime(2019, 7, 22, 4)
    else:
        for x in campaign_table["campaignRotateStageOpenTimes"]:
            if x["stageId"] == campaign["stageId"]:
                campaign_start_timestamp = x["startTs"]
                break
    # campaign reward
    campaign_reward = ItemInfoList()
    for break_ladder in campaign["breakLadders"]:
        for reward in break_ladder["rewards"]:
            if reward["type"] == "FURN":
                item_name = building_data["customData"]["furnitures"][reward["id"]]["name"]
            else:
                item_name = item_table["items"][reward["id"]]["name"]
            campaign_reward.append_item_info(item_name, reward["count"])

    print(generate_line(campaign_reward, f"{campaign_name}剿灭首次通关", campaign_start_timestamp, ["#剿灭作战首次通关"], 4, 6))
