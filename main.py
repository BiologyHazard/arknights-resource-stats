from models import ItemInfo, ResourceStats
from rewards import add_rewards

resource_stats = ResourceStats()

# 各种奖励
add_rewards(resource_stats)


resource_stats.add_tag("#剿灭作战", ["#剿灭作战首次通关", "#剿灭作战每周报酬"])
resource_stats.add_tag("#更新维护", ["#闪断更新", "#停机维护", "#不停机更新", "#异常情况修复"])
resource_stats.add_tag("#SideStory", ["SideStory首次通关", "SideStory赠送", "#SideStory商店", "SideStory物资箱", "#愚人号宝箱"])
resource_stats.add_tag("#故事集", [])
resource_stats.add_tag("#登录活动", [])
resource_stats.add_tag("#签到活动", [])
resource_stats.add_tag("#幸运墙", [])
resource_stats.add_tag("#主线活动", [])
resource_stats.add_tag("#危机合约",
                       ["#危机合约合约任务", "#危机合约常设兑换所", "#危机合约特设兑换所", "#危机合约物资补给", "#危机合约训练场"])
resource_stats.add_tag("#愚人节活动", [])
resource_stats.add_tag("#多维合作", [])
resource_stats.add_tag("#联锁竞赛", [])
resource_stats.add_tag("#引航者试炼", [])
resource_stats.add_tag("#纷争演绎", [])
resource_stats.add_tag("#尖灭测试作战", [])
resource_stats.add_tag("#罗德岛促融共竞", [])
resource_stats.add_tag("#其他游戏内限时活动", [])
resource_stats.add_tag("#游戏内限时活动", ["#SideStory", "#故事集", "#登录活动", "#签到活动", "#幸运墙", "#主线活动", "#危机合约", "#愚人节活动", "#多维合作", "#联锁竞赛", "#引航者试炼", "#纷争演绎", "尖灭测试作战", "#罗德岛促融共竞", "#其他游戏内限时活动"])
resource_stats.add_tag("#集成战略", [])
resource_stats.add_tag("#保全派驻", [])
resource_stats.add_tag("#生息演算", [])
resource_stats.add_tag("#游戏内常驻玩法", ["#集成战略", "#保全派驻", "#生息演算"])
resource_stats.add_tag("#网页活动", [])
resource_stats.add_tag("#免费邮件", ["#停机维护", "#闪断更新", "#游戏内邮件赠送", "#兑换码免费领取"])
resource_stats.add_tag("#森空岛签到", ["#森空岛常规签到", "#森空岛签到活动"])
resource_stats.add_tag("#森空岛", ["#森空岛签到", "#森空岛活动"])


if __name__ == '__main__':
    # result = resource_stats.query("2023-01-01 00:00:00+08:00", "2024-01-01 00:00:00+08:00", "!#森空岛活动")
    # result = resource_stats.query("2023-01-01 00:00:00+08:00", "2024-01-01 00:00:00+08:00", "!#森空岛活动")
    result = resource_stats.advanced_query("2023-01-01 00:00:00+08:00", "2024-10-01 00:00:00+08:00", "!#森空岛活动")
    # for item_name, item_data in result.items():
    #     print(f"{item_name}: {dict(item_data)}")
    print(result["高级凭证"])

    # from scripts.utils import item_name_to_info, item_type_display_name
    # import csv

    # def sort_key(item: ItemInfo):
    #     name, count = item
    #     count = f"{count}" if isinstance(count, int) else f"{count:.2f}"
    #     if name in item_name_to_info:
    #         id, type = item_name_to_info[name]
    #         return (item_type_display_name[type], name, count)
    #     elif name.endswith("的图鉴"):
    #         return ("干员的图鉴", name, count)
    #     elif name.endswith("的潜能"):
    #         return ("干员的潜能", name, count)
    #     else:
    #         return ("自定义道具", name, count)
    # result = sorted(sort_key(x) for x in result)

    # with open('temp.csv', 'w', newline='', encoding="utf-8") as csvfile:
    #     writer = csv.writer(csvfile, delimiter='\t')
    #     writer.writerow(['道具类型', '道具名称', '道具数量'])  # Write header row
    #     for type, name, count in result:
    #         writer.writerow([type, name, count])
