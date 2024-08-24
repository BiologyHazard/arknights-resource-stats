from models import ResourceStats
from rewards import add_rewards

resource_stats = ResourceStats()

# 各种奖励
add_rewards(resource_stats)


resource_stats.add_tag("#剿灭作战", ["#剿灭作战首次通关", "#剿灭作战每周报酬"])
resource_stats.add_tag("#SideStory", ["SideStory首次通关", "SideStory赠送", "#SideStory商店", "SideStory物资箱", "#愚人号宝箱"])
resource_stats.add_tag("#故事集", [])
resource_stats.add_tag("#登录活动", [])
resource_stats.add_tag("#签到活动", [])
resource_stats.add_tag("#幸运墙活动", [])
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
resource_stats.add_tag("#游戏内限时活动", ["#SideStory", "#故事集", "#登录活动", "#签到活动", "#幸运墙活动", "#主线活动", "#危机合约", "#愚人节活动", "#多维合作", "#联锁竞赛", "#引航者试炼", "#纷争演绎", "尖灭测试作战", "#罗德岛促融共竞", "#其他游戏内限时活动"])
resource_stats.add_tag("#游戏内常驻玩法", ["#集成战略", "#保全派驻", "#生息演算"])
resource_stats.add_tag("#网页活动", [])
resource_stats.add_tag("#免费邮件", ["#停服更新", "#闪断更新", "#游戏内邮件赠送", "#兑换码免费领取"])
resource_stats.add_tag("#森空岛签到", ["#森空岛常规签到", "#森空岛签到活动"])
resource_stats.add_tag("#森空岛", ["#森空岛签到", "#森空岛活动"])


if __name__ == '__main__':
    # result = resource_stats.query("2023-01-01 00:00:00+08:00", "2024-01-01 00:00:00+08:00", "!#森空岛活动")
    result = resource_stats.query("2023-01-01 00:00:00+08:00", "2024-01-01 00:00:00+08:00", )
    for name, count in result:
        print(f"{name}: {count}")
    # print(resource_stats.tags)
