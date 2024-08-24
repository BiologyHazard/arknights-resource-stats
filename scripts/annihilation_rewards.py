from collections.abc import Generator

from models import ItemInfoList
from scripts.excels import building_data, campaign_table, item_table, stage_table
from scripts.manager import Line, manager


@manager.register(
    file_name="annihilation",
    function_name="add_annihilation_first_clear_resources",
    import_str="from models import ResourceStats",
    comments='"""不计理智消耗，不计合成玉报酬"""',
)
def annihilation_rewards() -> Generator[Line, None, None]:
    for campaign in campaign_table["campaigns"].values():
        campaign_name = stage_table["stages"][campaign["stageId"]]["name"]
        # campaign start time
        if campaign_name in ("切尔诺伯格", "龙门外环"):
            campaign_start_time = "2019-04-30 10:00:00+08:00"
        elif campaign_name == "龙门市区":
            campaign_start_time = "2019-07-22 04:00:00+08:00"
        else:
            for x in campaign_table["campaignRotateStageOpenTimes"]:
                if x["stageId"] == campaign["stageId"]:
                    campaign_start_time = x["startTs"]
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

        yield campaign_reward, f"{campaign_name}剿灭首次通关", campaign_start_time, ["#剿灭作战首次通关"], 4, 6
