import sys
from typing import TypedDict

from scripts.excels import (activity_table, building_data, character_table,
                            display_meta_table, item_table, replicate_table, skin_table)

sys.path.append(r".")
from time_utils import to_CST_datetime  # NOQA: E402

avatar_dict = {avatar_info["avatarId"]: avatar_info for avatar_info in display_meta_table["playerAvatarData"]["avatarList"]}
background_dict = {background_info["bgId"]: background_info for background_info in display_meta_table["homeBackgroundData"]["homeBgDataList"]}


class Reward(TypedDict):
    type: str
    id: str
    count: int


def get_reward_type(reward: Reward) -> str:
    if reward["type"] == "NONE":
        if reward["id"].startswith("furni"):
            return "FURN"
        elif reward["id"].startswith("char"):
            return "CHAR"
        else:
            return "ITEM"
    else:
        return reward["type"]


def get_reward_name(reward: Reward) -> str:
    reward_type = get_reward_type(reward)
    reward_id = reward["id"]

    if reward_type == "CHAR_SKIN":
        return skin_table["charSkins"][reward_id]["displaySkin"]["skinName"]
    elif reward_type == "FURN":
        return building_data["customData"]["furnitures"][reward_id]["name"]
    elif reward_type == "CHAR":
        return character_table[reward_id]["name"]
    elif reward_type == "PLAYER_AVATAR":
        return avatar_dict[reward_id]["avatarItemName"]
    elif reward_type == "HOME_BACKGROUND":
        return background_dict[reward_id]["bgName"]
    elif reward_type == "ACT_CART_COMPONENT":
        return activity_table["carData"]["carDict"][reward_id]["name"]
    else:
        return item_table["items"][reward_id]["name"]


def get_event_name(event_id: str) -> str:
    event_basic_info = activity_table["basicInfo"][event_id]
    event_type = event_basic_info["type"]
    event_name = event_basic_info["name"]
    event_start_timestamp = event_basic_info["startTime"]
    event_start_datetime = to_CST_datetime(event_start_timestamp)

    if (event_type in ("CHECKIN_ONLY", "LOGIN_ONLY")
            and (name := activity_table["homeActConfig"][event_id]["actTopBarText"])):
        return f"{event_start_datetime.strftime("%Y-%m")} {name}"
    elif event_type in ("PRAY_ONLY", "BOSS_RUSH"):
        return f"{event_start_datetime.strftime("%Y-%m")} {event_name}"
    else:
        return event_name


def get_event_id_by_name(name: str) -> str:
    if len(name) > 4 and name[-4:].isdigit():
        name = f"{name[:-4]}·复刻"
    for event_id, event_basic_info in activity_table["basicInfo"].items():
        if event_basic_info["name"] == name:
            return event_id
    else:
        raise ValueError(f"Event {name} not found")


def get_furniture_id_by_name(name: str) -> str:
    for furniture_id, furniture_info in building_data["customData"]["furnitures"].items():
        if furniture_info["name"] == name:
            return furniture_id
    else:
        raise ValueError(f"Furniture {name} not found")


def furniture_to_intelligence_certificate(event_id: str, furniture_id: str) -> int:
    for replicate_item in replicate_table[event_id]["replicateList"]:
        if replicate_item["item"]["id"] == furniture_id:
            return replicate_item["replicateTokenItem"]["count"]
    else:
        raise ValueError(f"Replicate item {furniture_id} not found")
