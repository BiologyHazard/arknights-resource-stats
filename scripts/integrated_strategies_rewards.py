from collections.abc import Generator

from models import ItemInfoList
from scripts.excels import roguelike_topic_table
from scripts.manager import Line, manager
from scripts.utils import get_reward_item_info_list, Reward
from time_utils import to_CST_datetime


@manager.register(
    file_name="integrated_strategies",
    function_name="add_integrated_strategies_resources",
    import_str="""from models import ResourceStats

from .manager import manager""",
)
def integrated_strategies_rewards() -> Generator[Line, None, None]:
    for is_id in roguelike_topic_table["topics"]:
        is_info = roguelike_topic_table["topics"][is_id]
        is_detail = roguelike_topic_table["details"][is_id]
        is_name = is_info["name"]
        start_timestamp = is_info["startTime"]

        # 里程碑奖励
        i = 0
        for milestone_update in is_detail["milestoneUpdates"]:
            update_timestamp = milestone_update["updateTime"]
            update_timestamp = max(update_timestamp, start_timestamp)
            update_time = to_CST_datetime(update_timestamp)
            max_bp_level = milestone_update["maxBpLevel"]

            item_info_list = ItemInfoList()
            while i < len(is_detail["milestones"]) and is_detail["milestones"][i]["level"] <= max_bp_level:
                milestone = is_detail["milestones"][i]
                reward = Reward(id=milestone["itemID"], count=milestone["itemCount"], type=milestone["itemType"])
                item_info_list.extend(get_reward_item_info_list(reward))
                i += 1
            yield item_info_list, f"{is_name}里程碑奖励（{update_time.strftime("%Y年%m月")}）", update_timestamp, [f"#{is_name}", "#集成战略里程碑奖励"], 6

        # 月度奖励
        for month_team_id, month_team_data in is_detail["monthSquad"].items():
            update_timestamp = month_team_data["startTime"]
            update_timestamp = max(update_timestamp, start_timestamp)
            update_time = to_CST_datetime(update_timestamp)
            item_info_list = ItemInfoList()
            for reward in month_team_data["items"]:
                item_info_list.extend(get_reward_item_info_list(reward))
            yield item_info_list, f"{is_name}月度奖励（{update_time.strftime("%Y年%m月")}）", update_timestamp, [f"#{is_name}", "#集成战略月度奖励"], 6

        # 深入调查
        for challenge_id, challenge_data in is_detail["challenges"].items():
            challenge_name = challenge_data["challengeName"]
            challenge_timestamp = is_info["homeEntryDisplayData"][1]["startTs"]
            item_info_list = ItemInfoList()
            for reward in challenge_data["rewards"]:
                item_info_list.extend(get_reward_item_info_list(reward))
            yield item_info_list, f"{is_name}深入调查-{challenge_name}", challenge_timestamp, [f"#{is_name}", "#集成战略深入调查"], 6
