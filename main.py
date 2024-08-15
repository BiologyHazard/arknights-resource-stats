# from __future__ import annotations

from datetime import datetime, timedelta, timezone

from apscheduler.triggers.base import BaseTrigger
from apscheduler.triggers.combining import AndTrigger, OrTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

from models import CST, ItemInfo, ResourceStats, parse_items_str, format_items_str

II = ItemInfo


resource_stats = ResourceStats()
# 理智自动回复
# 假设每日 4 时回复 240 理智
resource_stats.add([II("理智", 240)],
                   "理智自动回复",
                   CronTrigger(hour=4, timezone=CST),
                   "#理智自动回复")

# 日常任务
daily_rewards_weekday = "龙门币×500 基础作战记录×3 龙门币×1000 技巧概要·卷1×2 招聘许可×1 基础作战记录×5 龙门币×2000 碳×3 加急许可×1 初级作战记录×5 合成玉×100 采购凭证×5 家具零件×60 PRTS剿灭代理卡×1 龙门币×6000 中级作战记录×6"
daily_rewards_weekend = "龙门币×500 基础作战记录×3 龙门币×1000 技巧概要·卷1×2 招聘许可×1 基础作战记录×5 龙门币×2000 碳×3 招聘许可×1 初级作战记录×5 合成玉×100 采购凭证×5 家具零件×60 PRTS剿灭代理卡×1 龙门币×6000 中级作战记录×6"
resource_stats.add(daily_rewards_weekday,
                   "日常任务（三周年之后）（周一至周五）",
                   CronTrigger(day_of_week="MON-FRI", hour=4, start_date="2022-05-02 04:00:00", timezone=CST),
                   "#日常任务")
resource_stats.add(daily_rewards_weekend,
                   "日常任务（三周年之后）（周六至周日）",
                   CronTrigger(day_of_week="SAT-SUN", hour=4, start_date="2022-05-02 04:00:00", timezone=CST),
                   "#日常任务")

# 周常任务
weekly_rewards = "龙门币×1000 基础作战记录×4 赤金×4 招聘许可×2 龙门币×2000 家具零件×50 初级作战记录×4 技巧概要·卷1×5 龙门币×4000 招聘许可×3 应急理智浓缩液×1 赤金×10 龙门币×6000 招聘许可×5 高级作战记录×4 家具零件×200 合成玉×500 采购凭证×30 资质凭证×20 应急理智浓缩液×1 中级作战记录×4 模组数据块×1 龙门币×10000 高级作战记录×5"
resource_stats.add(weekly_rewards,
                   "周常任务（三周年之后）",
                   CronTrigger(day_of_week="MON", hour=4, start_date="2022-05-02 04:00:00", timezone=CST),
                   "#周常任务")

# 每月签到
monthly_attendance_rewards = [
    II("龙门币", 2000),
    II("基础作战记录", 10),
    II("招聘许可", 2),
    II("采购凭证", 8),
    II("碳", 5),
    II("技巧概要·卷1", 5),
    II("赤金", 6),
    II("龙门币", 4000),
    II("初级作战记录", 10),
    II("加急许可", 2),
    II("资质凭证", 10),
    II("家具零件", 40),
    II("技巧概要·卷1", 10),
    II("赤金", 10),
    II("龙门币", 6000),
    II("中级作战记录", 6),
    II("寻访凭证", 1),
    II("采购凭证", 25),
    II("碳素", 6),
    II("技巧概要·卷2", 5),
    II("赤金", 15),
    II("龙门币", 8000),
    II("高级作战记录", 4),
    II("招聘许可", 3),
    II("高级凭证", 5),
    II("家具零件", 100),
    II("技巧概要·卷3", 6),
    II("芯片助剂", 1),
    II("龙门币", 10000),
    II("高级作战记录", 5),
    II("加急许可", 3),
]
for day_of_month, reward in enumerate(monthly_attendance_rewards, start=1):
    resource_stats.add(
        [reward],
        f"每月{day_of_month}日签到",
        CronTrigger(day=day_of_month, hour=4, timezone=CST),
        "#每月签到"
    )

# 资质凭证区
commendation_certificate_rewards = [
    II("寻访凭证", 2),
    II("招聘许可", 15),
    II("合成玉", 100 * 6),
    II("中级作战记录", 4 * 15),
    II("龙门币", 4000 * 15),
    II("赤金", 8 * 15),
    II("家具零件", 100 * 5),
    II("寻访凭证", 2),
    II("招聘许可", 20),
    II("资质凭证", -2690),
]
resource_stats.add(commendation_certificate_rewards,
                   "资质凭证区",
                   CronTrigger(day=1, start_date="2019-05-01 04:00:00", timezone=CST),
                   # 2019-05-01 04:00:00 实际上还没有开服
                   "#资质凭证区")

# 剿灭作战
# 剿灭作战首次通关


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
    datetime(2023, 9, 1): [II("研磨石", 1), II("RMA70-12", 1), II("轻锰矿", 1), II("固源岩组", 1), II("先锋芯片", 1)],  # 来自森空岛评论区，无法验证真实性
    # 2023-10 https://www.skland.com/article?id=171440
    datetime(2023, 10, 1): [II("晶体元件", 1), II("扭转醇", 1), II("全新装置", 1), II("聚酸酯组", 1), II("近卫芯片", 1)],
    # 2023-11 https://www.skland.com/article?id=245566
    datetime(2023, 11, 1): [II("半自然溶剂", 1), II("异铁组", 1), II("糖组", 1), II("酮凝集组", 1), II("重装芯片", 1)],
    # 2023-12 https://www.skland.com/article?id=1385373
    datetime(2023, 12, 1): [II("化合切削液", 1), II("凝胶", 1), II("炽合金", 1), II("转质盐组", 1), II("狙击芯片", 1)],
    # 2024-01 https://www.skland.com/article?id=1453080
    datetime(2024, 1, 1): [II("褐素纤维", 1), II("RMA70-12", 1), II("研磨石", 1), II("轻锰矿", 1), II("术师芯片", 1)],
    # 2024-02 https://www.skland.com/article?id=1534376
    datetime(2024, 2, 1): [II("环烃聚质", 1), II("固源岩组", 1), II("晶体元件", 1), II("扭转醇", 1), II("医疗芯片", 1)],
    # 2024-03 https://www.skland.com/article?id=1637185
    datetime(2024, 3, 1): [II("全新装置", 1), II("聚酸酯组", 1), II("半自然溶剂", 1), II("异铁组", 1), II("辅助芯片", 1)],
    # 2024-04 https://www.skland.com/article?id=1693252
    datetime(2024, 4, 1): [II("糖组", 1), II("酮凝集组", 1), II("化合切削液", 1), II("凝胶", 1), II("特种芯片", 1)],
    # 2024-05 https://www.skland.com/article?id=1833476
    datetime(2024, 5, 1): [II("炽合金", 1), II("转质盐组", 1), II("褐素纤维", 1), II("RMA70-12", 1), II("先锋芯片", 1)],
    # 2024-06 https://www.skland.com/article?id=1970187
    datetime(2024, 6, 1): [II("研磨石", 1), II("轻锰矿", 1), II("环烃聚质", 1), II("固源岩组", 1), II("近卫芯片", 1)],
    # 2024-07 https://www.skland.com/article?id=2037232
    datetime(2024, 7, 1): [II("晶体元件", 1), II("扭转醇", 1), II("全新装置", 1), II("聚酸酯组", 1), II("重装芯片", 1)],
    # 2024-08 https://www.skland.com/article?id=2117223
    datetime(2024, 8, 1): [II("半自然溶剂", 1), II("异铁组", 1), II("糖组", 1), II("酮凝集组", 1), II("狙击芯片", 1)],
}

for day_of_month, reward in enumerate(skland_attendance_rewards, start=1):
    if reward is None:
        continue
    resource_stats.add(
        [reward],
        f"森空岛常规签到（每月{day_of_month}日）",
        CronTrigger(day=day_of_month, hour=0, start_date="2023-09-01 00:00:00", timezone=CST),
        "#森空岛常规签到",
    )
for month, rewards in skland_rotating_attendance_rewards.items():
    for day_of_month, reward in zip(skland_rotating_attendance_reward_days, rewards):
        date = month.replace(day=day_of_month)
        resource_stats.add(
            [reward],
            f"森空岛常规签到（{date.strftime("%Y年%m月%d日")}）",
            DateTrigger(date, timezone=CST),
            "#森空岛常规签到",
        )

# 森空岛签到活动
# 首签奖励 https://www.skland.com/article?id=92162
first_attendance_rewards = [
    (datetime(2023, 9, 1), [II("合成玉", 500)]),
]
# 冬日签到福利活动 https://www.skland.com/article?id=1411630
冬日签到福利活动_rewards = [
    (datetime(2023, 12, 14), [II("龙门币", 3000)]),
    (datetime(2023, 12, 15), [II("合成玉", 100)]),
    (datetime(2023, 12, 16), [II("初级作战记录", 3)]),
    (datetime(2023, 12, 17), [II("合成玉", 100)]),
    (datetime(2023, 12, 18), [II("技巧概要·卷2", 2)]),
    (datetime(2023, 12, 19), [II("合成玉", 100)]),
    (datetime(2023, 12, 20), [II("招聘许可", 1)]),
]
# 春日签到福利活动 https://www.skland.com/article?id=1711375
春日签到福利活动_rewards = [
    (datetime(2024, 4, 8), [II("龙门币", 3000)]),
    (datetime(2024, 4, 9), [II("合成玉", 100)]),
    (datetime(2024, 4, 10), [II("初级作战记录", 3)]),
    (datetime(2024, 4, 11), [II("合成玉", 100)]),
    (datetime(2024, 4, 12), [II("技巧概要·卷2", 2)]),
    (datetime(2024, 4, 13), [II("合成玉", 100)]),
    (datetime(2024, 4, 14), [II("招聘许可", 1)]),
]
for date, rewards in first_attendance_rewards:
    resource_stats.add(
        rewards,
        "森空岛首签奖励",
        DateTrigger(date, timezone=CST),
        "#森空岛首签奖励",
    )
for date, rewards in 冬日签到福利活动_rewards:
    resource_stats.add(
        rewards,
        f"森空岛冬日签到福利活动（{date.strftime("%Y年%m月%d日")}）",
        DateTrigger(date, timezone=CST),
        "#森空岛冬日签到福利活动",
    )
for date, rewards in 春日签到福利活动_rewards:
    resource_stats.add(
        rewards,
        f"森空岛春日签到福利活动（{date.strftime("%Y年%m月%d日")}）",
        DateTrigger(date, timezone=CST),
        "#森空岛春日签到福利活动",
    )

# 森空岛活动
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
    (datetime(2024, 1, 27), 年夜饭_daily_rewards),
    (datetime(2024, 1, 28), 年夜饭_daily_rewards),
    (datetime(2024, 1, 29), 年夜饭_daily_rewards),
    (datetime(2024, 1, 30), 年夜饭_daily_rewards),
    (datetime(2024, 1, 31), 年夜饭_daily_rewards),
]
# 噼啪 https://www.skland.com/article?id=1525493
# 公示概率：龙门币×3000 30%，合成玉×100 5%，招聘许可×1 20%，技巧概要·卷2×3 20%，初级作战记录×3 20%，实物奖励 5%
# 此处假设龙门币的概率为 35%
噼啪_rewards = [
    (datetime(2024, 2, 1), [II("龙门币", 3000 * (0.35 + 0.05)),
                            II("合成玉", 100 * 0.05),
                            II("招聘许可", 1 * 0.20),
                            II("技巧概要·卷2", 3 * 0.20),
                            II("初级作战记录", 3 * 0.20)]),
]
# 我们的故事 https://www.skland.com/article?id=1792523
# 奖品清单中有其他游戏道具，但是有数量上限，无法得知具体概率，认为中奖概率为 0
我们的故事_rewards = [
    (datetime(2024, 4, 27), [II("龙门币", 3000),
                             II("龙门币", 3000),
                             II("龙门币", 3000),
                             II("龙门币", 3000),
                             II("龙门币", 3000)]),
]
# 博士在哪里 https://www.skland.com/article?id=1837102
# 奖品清单中有其他游戏道具，但是有数量上限，无法得知具体概率，认为必中龙门币
博士在哪里_rewards = [
    (datetime(2024, 5, 3, 8, 30), [II("龙门币", 3000)]),
]
# 佩佩的礼物 https://www.skland.com/article?id=2106023
# 奖品清单中有其他游戏道具，但是有数量上限，无法得知具体概率，认为必中龙门币
佩佩的礼物_rewards = [
    (datetime(2024, 7, 27), [II("龙门币", 20000)]),
]
for date, rewards in 感谢庆典许下心愿_rewards:
    resource_stats.add(
        rewards,
        f"森空岛感谢庆典许下心愿活动",
        DateTrigger(date, timezone=CST),
        "#森空岛感谢庆典许下心愿活动",
    )
for date, rewards in 年夜饭_rewards:
    resource_stats.add(
        rewards,
        f"森空岛年夜饭活动（{date.strftime('%Y年%m月%d日')}）",
        DateTrigger(date, timezone=CST),
        "#森空岛年夜饭活动",
    )
for date, rewards in 噼啪_rewards:
    resource_stats.add(
        rewards,
        f"森空岛噼啪活动",
        DateTrigger(date, timezone=CST),
        "#森空岛噼啪活动",
    )
for date, rewards in 我们的故事_rewards:
    resource_stats.add(
        rewards,
        f"森空岛我们的故事活动",
        DateTrigger(date, timezone=CST),
        "#森空岛我们的故事活动",
    )
for date, rewards in 博士在哪里_rewards:
    resource_stats.add(
        rewards,
        f"森空岛博士在哪里活动",
        DateTrigger(date, timezone=CST),
        "#森空岛博士在哪里活动",
    )
for date, rewards in 佩佩的礼物_rewards:
    resource_stats.add(
        rewards,
        f"森空岛佩佩的礼物活动",
        DateTrigger(date, timezone=CST),
        "#森空岛佩佩的礼物活动",
    )

resource_stats.add_tag("#森空岛签到活动", ["#森空岛首签奖励", "#森空岛冬日签到福利活动", "#森空岛春日签到福利活动"])
resource_stats.add_tag("#森空岛签到", ["#森空岛常规签到", "#森空岛签到活动"])
resource_stats.add_tag("#森空岛活动", ["#森空岛感谢庆典许下心愿活动",
                                  "#森空岛年夜饭活动",
                                  "#森空岛噼啪活动",
                                  "#森空岛我们的故事活动",
                                  "#森空岛博士在哪里活动",
                                  "#森空岛佩佩的礼物活动"])
resource_stats.add_tag("#森空岛", ["#森空岛签到", "#森空岛活动"])


if __name__ == '__main__':
    exit()
    result = resource_stats.query("2023-01-01 00:00:00", "2024-01-01 00:00:00", "!#森空岛活动")
    for name, count in result:
        print(f"{name}: {count}")
    print(resource_stats.tags)
