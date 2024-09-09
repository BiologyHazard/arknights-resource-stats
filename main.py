from models import ItemInfo, ResourceStats
from rewards import add_rewards

resource_stats = ResourceStats()

# 各种奖励
add_rewards(resource_stats)

resource_stats.add_tag("#免费资源", ["#开始熟悉罗德岛", "#欢迎回到罗德岛", "#理智自动回复", "#基建", "#公开招募", "#干员寻访", "#每月签到", "#干员页面", "#任务", "#档案", "#采购中心", "#终端", "#活动", "#邮件"])
resource_stats.add_tag("#开始熟悉罗德岛", [])
resource_stats.add_tag("#欢迎回到罗德岛", [])
# resource_stats.add_tag("#理智自动回复", [])
# resource_stats.add_tag("#基建", [])
resource_stats.add_tag("#公开招募", [])
resource_stats.add_tag("#干员寻访", [])
resource_stats.add_tag("#干员页面", ["#悖论模拟", "#干员异格任务"])
resource_stats.add_tag("#干员异格任务", [])
resource_stats.add_tag("#任务", ["#见习任务", "#日常任务", "#周常任务", "#主线任务"])
resource_stats.add_tag("#见习任务", [])
resource_stats.add_tag("#档案", ["#光荣之路", "#训练场", "#情报处理室", "#关系网"])
resource_stats.add_tag("#光荣之路", [])
# resource_stats.add_tag("#训练场", [])
resource_stats.add_tag("#情报处理室", ["#特别行动记述"])
resource_stats.add_tag("#特别行动记述", ["#故事集记录修复", "#故事集剧情解锁报酬"])
resource_stats.add_tag("#故事集记录修复", [])
# resource_stats.add_tag("#故事集剧情解锁报酬", [])
resource_stats.add_tag("#关系网", [])
resource_stats.add_tag("#采购中心", ["#组合包", "#时装商店", "#凭证交易所", "#家具商店", "#信用交易所"])
resource_stats.add_tag("#组合包", ["#强化包", "#专业强化包", "#ID信息更新礼包"])
resource_stats.add_tag("#强化包", [])
resource_stats.add_tag("#专业强化包", [])
# resource_stats.add_tag("#ID信息更新礼包", [])
resource_stats.add_tag("#时装商店", [])
resource_stats.add_tag("#凭证交易所", ["#资质凭证区", "#高级凭证区", "#通用凭证区", "#采购凭证区", "#寻访数据契约商店", "#寻访参数模型商店", "#情报凭证区", "#信物兑换凭证"])
# resource_stats.add_tag("#资质凭证区", [])
resource_stats.add_tag("#高级凭证区", [])
resource_stats.add_tag("#通用凭证区", [])
resource_stats.add_tag("#采购凭证区", [])
resource_stats.add_tag("#寻访数据契约商店", [])
resource_stats.add_tag("#寻访参数模型商店", [])
# resource_stats.add_tag("#情报凭证区", [])
resource_stats.add_tag("#信物兑换凭证", ["#赠送干员信物兑换凭证", "#采购凭证区干员信物兑换凭证"])
# resource_stats.add_tag("#赠送干员信物兑换凭证", [])
# resource_stats.add_tag("#采购凭证区干员信物兑换凭证", [])
resource_stats.add_tag("#家具商店", [])
resource_stats.add_tag("#信用交易所", [])
resource_stats.add_tag("#终端", ['#主题曲', '#插曲、别传', '#资源收集', '#常态事务', '#长期探索', '#周期挑战'])
resource_stats.add_tag("#主题曲", ["#主题曲新增章节", "#主题曲作战首次通关", "#主题曲记录点", "#隐秘战线", "#尘封密室"])
resource_stats.add_tag("#常态事务", ["#剿灭作战", "#保全派驻"])
resource_stats.add_tag("#剿灭作战", ["#剿灭作战首次通关", "#剿灭作战每周报酬"])
resource_stats.add_tag("#保全派驻", ["#旧保全派驻", "#现在的保全派驻"])
resource_stats.add_tag("#现在的保全派驻", ["#保全派驻首次清理奖励", "#保全派驻任务", "#保全派驻酬劳"])
resource_stats.add_tag("#长期探索", ["#集成战略", "#生息演算"])
resource_stats.add_tag("#集成战略", ["#集成战略里程碑奖励", "#集成战略月度小队", "#集成战略深入调查"])
resource_stats.add_tag("#生息演算", ["#沙中之火", "#沙洲遗闻"])
resource_stats.add_tag("#沙中之火", ["#沙中之火里程碑奖励"])
resource_stats.add_tag("#沙洲遗闻", ["#沙洲遗闻商店", "#沙洲遗闻战争浪潮", "#沙洲遗闻险途"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
resource_stats.add_tag("#", ["#", "#", "#", "#", "#", "#", "#", "#"])
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
resource_stats.add_tag("#游戏内限时活动", ["#SideStory", "#故事集", "#登录活动", "#签到活动", "#幸运墙", "#主线活动", "#危机合约", "#愚人节活动", "#多维合作", "#联锁竞赛", "#引航者试炼", "#纷争演绎", "#尖灭测试作战", "#罗德岛促融共竞", "#其他游戏内限时活动"])
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
