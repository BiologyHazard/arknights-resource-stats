from datetime import datetime

from models import ItemInfo as II
from models import ResourceStats
from time_utils import CST, to_CST_datetime
from triggers import CronTrigger

from .manager import manager


@manager.register
def add_skland_attendance_resources(resource_stats: ResourceStats):
    # 森空岛签到
    # 森空岛常规签到
    skland_attendance_rewards = [
        II("初级作战记录", 3),
        II("龙门币", 500),
        II("技巧概要·卷2", 2),
        II("合成玉", 80),
        II("初级作战记录", 3),
        II("龙门币", 500),
        None,  # 指定精英材料
        None,  # 指定精英材料
        II("中级作战记录", 2),
        II("龙门币", 500),
        II("技巧概要·卷2", 2),
        II("合成玉", 100),
        II("中级作战记录", 2),
        II("龙门币", 1000),
        None,  # 指定精英材料
        None,  # 指定精英材料
        II("中级作战记录", 4),
        II("龙门币", 1000),
        II("技巧概要·卷3", 1),
        II("合成玉", 120),
        II("高级作战记录", 2),
        II("龙门币", 1000),
        II("技巧概要·卷3", 1),
        None,  # 指定芯片
        II("高级作战记录", 2),
        II("龙门币", 1000),
        II("龙门币", 1000),
        II("龙门币", 1000),
        II("龙门币", 500),
        II("龙门币", 500),
        II("龙门币", 500),
    ]
    skland_rotating_attendance_reward_days = [7, 8, 15, 16, 24]
    skland_rotating_attendance_rewards = {
        # 2023-09 https://www.skland.com/article?id=92162
        (2023, 9): "研磨石×1 RMA70-12×1 轻锰矿×1 固源岩组×1 先锋芯片×1",  # 来自森空岛评论区，无法验证真实性
        # 2023-10 https://www.skland.com/article?id=171440
        (2023, 10): "晶体元件×1 扭转醇×1 全新装置×1 聚酸酯组×1 近卫芯片×1",
        # 2023-11 https://www.skland.com/article?id=245566
        (2023, 11): "半自然溶剂×1 异铁组×1 糖组×1 酮凝集组×1 重装芯片×1",
        # 2023-12 https://www.skland.com/article?id=1385373
        (2023, 12): "化合切削液×1 凝胶×1 炽合金×1 转质盐组×1 狙击芯片×1",
        # 2024-01 https://www.skland.com/article?id=1453080
        (2024, 1): "褐素纤维×1 RMA70-12×1 研磨石×1 轻锰矿×1 术师芯片×1",
        # 2024-02 https://www.skland.com/article?id=1534376
        (2024, 2): "环烃聚质×1 固源岩组×1 晶体元件×1 扭转醇×1 医疗芯片×1",
        # 2024-03 https://www.skland.com/article?id=1637185
        (2024, 3): "全新装置×1 聚酸酯组×1 半自然溶剂×1 异铁组×1 辅助芯片×1",
        # 2024-04 https://www.skland.com/article?id=1693252
        (2024, 4): "糖组×1 酮凝集组×1 化合切削液×1 凝胶×1 特种芯片×1",
        # 2024-05 https://www.skland.com/article?id=1833476
        (2024, 5): "炽合金×1 转质盐组×1 褐素纤维×1 RMA70-12×1 先锋芯片×1",
        # 2024-06 https://www.skland.com/article?id=1970187
        (2024, 6): "研磨石×1 轻锰矿×1 环烃聚质×1 固源岩组×1 近卫芯片×1",
        # 2024-07 https://www.skland.com/article?id=2037232
        (2024, 7): "晶体元件×1 扭转醇×1 全新装置×1 聚酸酯组×1 重装芯片×1",
        # 2024-08 https://www.skland.com/article?id=2117223
        (2024, 8): "半自然溶剂×1 异铁组×1 糖组×1 酮凝集组×1 狙击芯片×1",
    }

    for day_of_month, reward in enumerate(skland_attendance_rewards, start=1):
        if reward is None:
            continue
        resource_stats.add(
            [reward],
            f"森空岛常规签到（每月{day_of_month}日）",
            CronTrigger(day=day_of_month, hour=0, start_time="2023-09-01 00:00:00+08:00", timezone=CST),
            "#森空岛常规签到",
        )
    for (year, month), rewards in skland_rotating_attendance_rewards.items():
        for day_of_month, reward in zip(skland_rotating_attendance_reward_days, rewards.split()):
            date = datetime(year, month, day_of_month, tzinfo=CST)
            resource_stats.add(
                [reward],
                f"森空岛常规签到（{date.strftime("%Y年%m月%d日")}）",
                date,
                "#森空岛常规签到",
            )

    # 森空岛签到活动
    # 首签奖励 https://www.skland.com/article?id=92162
    first_attendance_rewards = [
        ("2023-09-01 00:00:00+08:00", "合成玉×500"),
    ]
    # 冬日签到福利活动 https://www.skland.com/article?id=1411630
    冬日签到福利活动_rewards = [
        ("2023-12-14 00:00:00+08:00", "龙门币×3000"),
        ("2023-12-15 00:00:00+08:00", "合成玉×100"),
        ("2023-12-16 00:00:00+08:00", "初级作战记录×3"),
        ("2023-12-17 00:00:00+08:00", "合成玉×100"),
        ("2023-12-18 00:00:00+08:00", "技巧概要·卷2×2"),
        ("2023-12-19 00:00:00+08:00", "合成玉×100"),
        ("2023-12-20 00:00:00+08:00", "招聘许可×1"),
    ]
    # 春日签到福利活动 https://www.skland.com/article?id=1711375
    春日签到福利活动_rewards = [
        ("2024-04-08 00:00:00+08:00", "龙门币×3000"),
        ("2024-04-09 00:00:00+08:00", "合成玉×100"),
        ("2024-04-10 00:00:00+08:00", "初级作战记录×3"),
        ("2024-04-11 00:00:00+08:00", "合成玉×100"),
        ("2024-04-12 00:00:00+08:00", "技巧概要·卷2×2"),
        ("2024-04-13 00:00:00+08:00", "合成玉×100"),
        ("2024-04-14 00:00:00+08:00", "招聘许可×1"),
    ]
    for date, rewards in first_attendance_rewards:
        resource_stats.add(
            rewards,
            "森空岛首签奖励",
            date,
            "#森空岛首签奖励", "#森空岛签到活动",
        )
    for date, rewards in 冬日签到福利活动_rewards:
        date = to_CST_datetime(date)
        resource_stats.add(
            rewards,
            f"森空岛冬日签到福利活动（{date.strftime("%Y年%m月%d日")}）",
            date,
            "#森空岛冬日签到福利活动", "#森空岛签到活动",
        )
    for date, rewards in 春日签到福利活动_rewards:
        date = to_CST_datetime(date)
        resource_stats.add(
            rewards,
            f"森空岛春日签到福利活动（{date.strftime("%Y年%m月%d日")}）",
            date,
            "#森空岛春日签到福利活动", "#森空岛签到活动",
        )
    # 森空岛一周年签到福利活动 https://www.skland.com/article?id=2193257
    resource_stats.add("龙门币×3000", "森空岛一周年签到福利活动（2024-09-06）",
                       "2024-09-06 00:00:00+08:00", "#森空岛一周年签到福利活动", "#森空岛签到活动")
    resource_stats.add("合成玉×100", "森空岛一周年签到福利活动（2024-09-07）",
                       "2024-09-07 00:00:00+08:00", "#森空岛一周年签到福利活动", "#森空岛签到活动")
    resource_stats.add("初级作战记录×3", "森空岛一周年签到福利活动（2024-09-08）",
                       "2024-09-08 00:00:00+08:00", "#森空岛一周年签到福利活动", "#森空岛签到活动")
    resource_stats.add("合成玉×100", "森空岛一周年签到福利活动（2024-09-09）",
                       "2024-09-09 00:00:00+08:00", "#森空岛一周年签到福利活动", "#森空岛签到活动")
    resource_stats.add("技巧概要·卷2×2", "森空岛一周年签到福利活动（2024-09-10）",
                       "2024-09-10 00:00:00+08:00", "#森空岛一周年签到福利活动", "#森空岛签到活动")
    resource_stats.add("合成玉×100", "森空岛一周年签到福利活动（2024-09-11）",
                       "2024-09-11 00:00:00+08:00", "#森空岛一周年签到福利活动", "#森空岛签到活动")
    resource_stats.add("招聘许可×1", "森空岛一周年签到福利活动（2024-09-12）",
                       "2024-09-12 00:00:00+08:00", "#森空岛一周年签到福利活动", "#森空岛签到活动")


@manager.register
def add_skland_event_resources(resource_stats: ResourceStats):
    """森空岛活动"""
    # 感谢庆典许下心愿 https://www.skland.com/article?id=260953
    # 公示概率：龙门币×3000 32.9898%，合成玉×100 1%，家具零件×100 25%，技巧概要·卷2×3 20%，初级作战记录×3 20%，实物奖励 1.0102%
    # 此处假设龙门币的概率为 34%
    感谢庆典许下心愿_rewards = [
        (datetime(2023, 11, 3), [II("龙门币", 3000 * (0.3298 + 0.0101)),
                                 II("合成玉", 100 * 0.01),
                                 II("家具零件", 100 * 0.25),
                                 II("技巧概要·卷2", 3 * 0.20),
                                 II("初级作战记录", 3 * 0.20)]),
    ]
    # 年夜饭 https://www.skland.com/article?id=1502786
    # 公示概率：龙门币×3000 28%，合成玉×100 2%，招聘许可×1 20%，技巧概要·卷2×3 20%，初级作战记录×3 20%，实物奖励 10%
    # 此处假设龙门币的概率为 38%
    年夜饭_daily_rewards = [
        II("龙门币", 3000 * (0.28 + 0.10)),
        II("合成玉", 100 * 0.02),
        II("招聘许可", 1 * 0.20),
        II("技巧概要·卷2", 3 * 0.20),
        II("初级作战记录", 3 * 0.20),
    ]
    年夜饭_rewards = [
        ("2024-01-27 00:00:00+08:00", 年夜饭_daily_rewards),
        ("2024-01-28 00:00:00+08:00", 年夜饭_daily_rewards),
        ("2024-01-29 00:00:00+08:00", 年夜饭_daily_rewards),
        ("2024-01-30 00:00:00+08:00", 年夜饭_daily_rewards),
        ("2024-01-31 00:00:00+08:00", 年夜饭_daily_rewards),
    ]
    # 噼啪 https://www.skland.com/article?id=1525493
    # 公示概率：龙门币×3000 30%，合成玉×100 5%，招聘许可×1 20%，技巧概要·卷2×3 20%，初级作战记录×3 20%，实物奖励 5%
    # 此处假设龙门币的概率为 35%
    噼啪_rewards = [
        ("2024-02-01 00:00:00+08:00", [II("龙门币", 3000 * (0.35 + 0.05)),
                                       II("合成玉", 100 * 0.05),
                                       II("招聘许可", 1 * 0.20),
                                       II("技巧概要·卷2", 3 * 0.20),
                                       II("初级作战记录", 3 * 0.20)]),
    ]
    # 我们的故事 https://www.skland.com/article?id=1792523
    # 奖品清单中有其他游戏道具，但是有数量上限，无法得知具体概率，认为必中龙门币
    我们的故事_rewards = [
        ("2024-04-27 00:00:00+08:00", [II("龙门币", 3000),
                                       II("龙门币", 3000),
                                       II("龙门币", 3000),
                                       II("龙门币", 3000),
                                       II("龙门币", 3000)]),
    ]
    # 博士在哪里 https://www.skland.com/article?id=1837102
    # 奖品清单中有其他游戏道具，但是有数量上限，无法得知具体概率，认为必中龙门币
    博士在哪里_rewards = [
        ("2024-05-03 08:30:00+08:00", [II("龙门币", 3000)]),
    ]
    # 佩佩的礼物 https://www.skland.com/article?id=2106023
    # 奖品清单中有其他游戏道具，但是有数量上限，无法得知具体概率，认为必中龙门币
    佩佩的礼物_rewards = [
        ("2024-07-27 00:00:00+08:00", [II("龙门币", 20000)]),
    ]
    for date, rewards in 感谢庆典许下心愿_rewards:
        resource_stats.add(
            rewards,
            f"森空岛感谢庆典许下心愿活动",
            date,
            "#森空岛感谢庆典许下心愿活动", "#森空岛活动",
        )
    for date, rewards in 年夜饭_rewards:
        date = to_CST_datetime(date)
        resource_stats.add(
            rewards,
            f"森空岛年夜饭活动（{date.strftime('%Y年%m月%d日')}）",
            date,
            "#森空岛年夜饭活动", "#森空岛活动",
        )
    for date, rewards in 噼啪_rewards:
        resource_stats.add(
            rewards,
            f"森空岛噼啪活动",
            date,
            "#森空岛噼啪活动", "#森空岛活动",
        )
    for date, rewards in 我们的故事_rewards:
        resource_stats.add(
            rewards,
            f"森空岛我们的故事活动",
            date,
            "#森空岛我们的故事活动", "#森空岛活动",
        )
    for date, rewards in 博士在哪里_rewards:
        resource_stats.add(
            rewards,
            f"森空岛博士在哪里活动",
            date,
            "#森空岛博士在哪里活动", "#森空岛活动",
        )
    for date, rewards in 佩佩的礼物_rewards:
        resource_stats.add(
            rewards,
            f"森空岛佩佩的礼物活动",
            date,
            "#森空岛佩佩的礼物活动", "#森空岛活动",
        )
