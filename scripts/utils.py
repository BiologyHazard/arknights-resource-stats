from typing import TypedDict

from models import ItemInfoList
from scripts.excels import (activity_table, building_data, character_table,
                            display_meta_table, item_table, replicate_table, skin_table)
from time_utils import to_CST_datetime

avatar_dict = {avatar_info["avatarId"]: avatar_info for avatar_info in display_meta_table["playerAvatarData"]["avatarList"]}
background_dict = {background_info["bgId"]: background_info for background_info in display_meta_table["homeBackgroundData"]["homeBgDataList"]}
theme_dict = {theme_info["id"]: theme_info for theme_info in display_meta_table["homeBackgroundData"]["themeList"]}

item_name_to_info: dict[str, tuple[str, str]] = {}
item_name_to_info.update((data["name"], (id, data["itemType"])) for id, data in item_table["items"].items())
item_name_to_info.update((data["displaySkin"]["skinName"], (id, "CHAR_SKIN")) for id, data in skin_table["charSkins"].items())
item_name_to_info.update((data["name"], (id, "FURN")) for id, data in building_data["customData"]["furnitures"].items())
item_name_to_info.update((data["name"], (id, "CHAR")) for id, data in character_table.items() if data["profession"] not in ("TOKEN", "TRAP"))
item_name_to_info.update((data["avatarItemName"], (id, "PLAYER_AVATAR")) for id, data in avatar_dict.items())
item_name_to_info.update((data["bgName"], (id, "HOME_BACKGROUND")) for id, data in background_dict.items())
item_name_to_info.update((data["name"], (id, "ACT_CART_COMPONENT")) for id, data in activity_table["carData"]["carDict"].items())
item_name_to_info.update((data["tmName"], (id, "HOME_THEME")) for id, data in theme_dict.items())
item_name_to_info.update((data["name"], (id, "NAME_CARD_SKIN")) for id, data in display_meta_table["nameCardV2Data"]["skinData"].items())

item_type_display_name = {
    "ACTIVITY_ITEM": "活动道具",
    "ACTIVITY_POTENTIAL": "干员的文件夹",
    "ACT_CART_COMPONENT": "自走车装备",
    "AP_BASE": "无人机",
    "AP_GAMEPLAY": "理智",
    "AP_ITEM": "理智道具",
    "AP_SUPPLY": "理智道具",
    "CARD_EXP": "作战记录",
    "CHAR": "干员的合同",
    "CHAR_SKIN": "时装",
    "CLASSIC_FES_PICK_TIER_5": "中坚甄选5星干员",
    "CLASSIC_FES_PICK_TIER_6": "中坚甄选6星干员",
    "CLASSIC_SHD": "通用凭证",
    "CLASSIC_TKT_GACHA": "中坚寻访凭证",
    "CLASSIC_TKT_GACHA_10": "十连中坚寻访凭证",
    "CRS_SHOP_COIN_V2": "晶体合约赏金",
    "DIAMOND": "至纯源石",
    "DIAMOND_SHD": "合成玉",
    "EPGS_COIN": "寻访参数模型",
    "ET_STAGE": "黑曜石节门票",
    "EXCLUSIVE_TKT_GACHA": "如死亦终寻访凭证",
    "EXCLUSIVE_TKT_GACHA_10": "如死亦终十连寻访凭证",
    "EXP_PLAYER": "声望",
    "EXTERMINATION_AGENT": "PRTS剿灭代理卡",
    "FAVOR_ADD_ITEM": "信赖提升道具",
    "FURN": "家具",
    "GOLD": "龙门币",
    "HGG_SHD": "高级凭证",
    "HOME_BACKGROUND": "首页场景",
    "HOME_THEME": "界面主题",
    "ITEM_PACK": "物品整合包",
    "LGG_SHD": "资质凭证",
    "LIMITED_BUFF": "后勤特别许可证",
    "LIMITED_TKT_GACHA_10": "限定寻访十连寻访凭证",
    "LINKAGE_TKT_GACHA_10": "合作限定寻访十连寻访凭证",
    "LMTGS_COIN": "寻访数据契约",
    "MATERIAL": "材料",
    "MATERIAL_ISSUE_VOUCHER": "材料提货券",
    "MCARD_VOUCHER": "月卡兑换凭证",
    "MEDAL": "蚀刻章",
    "NAME_CARD_SKIN": "个人名片",
    "NEW_PROGRESS": "开服累登券",
    "OPTIONAL_VOUCHER_PICK": "芯片自选",
    "PLAYER_AVATAR": "头像",
    "RENAMING_CARD": "ID信息更新卡",
    "REP_COIN": "情报凭证",
    "RETRO_COIN": "事相结晶",
    "RETURN_CREDIT": "二次认证徽记",
    "RETURN_PROGRESS": "回流累登券",
    "RL_COIN": "集成战略代币",
    "SANDBOX_TOKEN": "生息演算代币",
    "SOCIAL_PT": "信用",
    "TKT_GACHA": "寻访凭证",
    "TKT_GACHA_10": "十连寻访凭证",
    "TKT_GACHA_PRSV": "预约干员随机4选1",
    "TKT_INST_FIN": "加急许可",
    "TKT_RECRUIT": "招聘许可",
    "TKT_TRY": "演习券",
    "UNI_COLLECTION": "家具收藏包",
    "VOUCHER_CGACHA": "新年寻访凭证",
    "VOUCHER_ELITE_II_4": "专业干员特训邀请函",
    "VOUCHER_ELITE_II_5": "资深干员特训邀请函",
    "VOUCHER_ELITE_II_6": "高级资深干员特训邀请函",
    "VOUCHER_FULL_POTENTIAL": "干员的私人信件",
    "VOUCHER_LEVELMAX_5": "资深干员特训装置",
    "VOUCHER_LEVELMAX_6": "高级资深干员特训装置",
    "VOUCHER_MGACHA": "物资补给",
    "VOUCHER_PICK": "干员自选券",
    "VOUCHER_SKILL_SPECIALLEVELMAX_4": "专业干员技巧集",
    "VOUCHER_SKILL_SPECIALLEVELMAX_5": "资深干员技巧集",
    "VOUCHER_SKILL_SPECIALLEVELMAX_6": "高级资深干员技巧集",
    "VOUCHER_SKIN": "时装自选凭证",
}


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
        name = skin_table["charSkins"][reward_id]["displaySkin"]["skinName"]
    elif reward_type == "FURN":
        name = building_data["customData"]["furnitures"][reward_id]["name"]
    elif reward_type == "CHAR":
        name = character_table[reward_id]["name"]
    elif reward_type == "PLAYER_AVATAR":
        name = avatar_dict[reward_id]["avatarItemName"]
    elif reward_type == "HOME_BACKGROUND":
        name = background_dict[reward_id]["bgName"]
    elif reward_type == "ACT_CART_COMPONENT":
        name = activity_table["carData"]["carDict"][reward_id]["name"]
    elif reward_type == "HOME_THEME":
        name = theme_dict[reward_id]["tmName"]
    elif reward_type == "NAME_CARD_SKIN":
        name = display_meta_table["nameCardV2Data"]["skinData"][reward_id]["name"]
    else:
        name = item_table["items"][reward_id]["name"]
    return name.strip("\n")


def get_reward_item_info_list(reward: Reward) -> ItemInfoList:
    reward_type = get_reward_type(reward)
    reward_id = reward["id"]
    reward_count = reward["count"]
    reward_name = get_reward_name(reward)

    item_info_list = ItemInfoList()
    if reward_type == "ITEM_PACK":  # 模组数据整合块、芯片组印刻仪等物品
        item_pack_data = item_table["itemPackInfos"][reward_id]
        for content in item_pack_data["content"]:
            content = Reward(type=content["type"], id=content["id"], count=content["count"] * reward_count)
            item_info_list.extend(get_reward_item_info_list(content))
    elif reward_type == "UNI_COLLECTION":  # 家具收藏包
        uni_collection_data = item_table["uniCollectionInfo"][reward_id]
        for item in uni_collection_data["uniqueItem"]:
            item = Reward(type=item["type"], id=item["id"], count=item["count"] * reward_count)
            item_info_list.extend(get_reward_item_info_list(item))
    else:
        item_info_list.append_item_info(reward_name, reward_count)
    return item_info_list


def get_event_name(event_id: str) -> str:
    event_basic_info = activity_table["basicInfo"][event_id]
    event_type = event_basic_info["type"]
    event_name = event_basic_info["name"]
    event_start_timestamp = event_basic_info["startTime"]
    event_start_datetime = to_CST_datetime(event_start_timestamp)

    if (event_type in ("CHECKIN_ONLY", "LOGIN_ONLY", "PRAY_ONLY")
            and (name := activity_table["homeActConfig"][event_id]["actTopBarText"])):
        return f"{event_start_datetime.strftime("%Y-%m")} {name}"
    elif event_type in ("BOSS_RUSH", ):
        return f"{event_start_datetime.strftime("%Y-%m")} {event_name}"
    else:
        return event_name


def get_event_start_timestamp(event_id: str) -> int:
    event_basic_info = activity_table["basicInfo"][event_id]
    event_start_timestamp = event_basic_info["startTime"]
    return event_start_timestamp


def get_event_id_by_name(name: str) -> str:
    if len(name) > 4 and name[-4:].isdigit():
        name = f"{name[:-4]}·复刻"
    if name == "理想城长夏狂欢季·复刻":
        name = "理想城：长夏狂欢季·复刻"
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
