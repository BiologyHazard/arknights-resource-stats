from datetime import datetime

from models import ItemInfo, ResourceStats
from rewards.annihilation import add_annihilation_first_clear_resources
from rewards.check_in import add_check_in_resources
from rewards.event_mission import add_event_mission_resources
from rewards.intelligence_store import add_intelligence_store_resources
from rewards.login import add_login_resources
from rewards.lucky_wall import add_lucky_wall_resources
from rewards.reclamation_algorithm import add_reclamation_algorithm_resources
from rewards.sidestory import (add_吾导先路_复刻_resources, add_将进酒_复刻_resources, add_春分_resources,
                               add_登临意_resources, add_落叶逐火_resources, add_起源行动_resources)
from rewards.trials_for_navigator import add_trials_for_navigator_resources
from time_utils import CST, to_CST_datetime
from triggers import CronTrigger

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
                   CronTrigger(day_of_week="MON-FRI", hour=4, start_time="2022-05-02 04:00:00+08:00", timezone=CST),
                   "#日常任务")
resource_stats.add(daily_rewards_weekend,
                   "日常任务（三周年之后）（周六至周日）",
                   CronTrigger(day_of_week="SAT-SUN", hour=4, start_time="2022-05-02 04:00:00+08:00", timezone=CST),
                   "#日常任务")

# 周常任务
weekly_rewards = "龙门币×1000 基础作战记录×4 赤金×4 招聘许可×2 龙门币×2000 家具零件×50 初级作战记录×4 技巧概要·卷1×5 龙门币×4000 招聘许可×3 应急理智浓缩液×1 赤金×10 龙门币×6000 招聘许可×5 高级作战记录×4 家具零件×200 合成玉×500 采购凭证×30 资质凭证×20 应急理智浓缩液×1 中级作战记录×4 模组数据块×1 龙门币×10000 高级作战记录×5"
resource_stats.add(weekly_rewards,
                   "周常任务（三周年之后）",
                   CronTrigger(day_of_week="MON", hour=4, start_time="2022-05-02 04:00:00+08:00", timezone=CST),
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
                   CronTrigger(day=1, start_time="2019-05-01 04:00:00+08:00", timezone=CST),
                   "#资质凭证区")

# 情报凭证区
add_intelligence_store_resources(resource_stats)

# 剿灭作战
# 剿灭作战首次通关
add_annihilation_first_clear_resources(resource_stats)

# 剿灭作战每周报酬
resource_stats.add(
    "合成玉×1800",
    "剿灭作战每周报酬",
    CronTrigger(day_of_week="MON", hour=4, start_time="2020-11-02 04:00:00+08:00", timezone=CST),
    "#剿灭作战每周报酬"
)

# 活动
# 活动任务
add_event_mission_resources(resource_stats)

# 将进酒·复刻
add_将进酒_复刻_resources(resource_stats)

# 登临意
add_登临意_resources(resource_stats)

# 春分
add_春分_resources(resource_stats)

# 吾导先路·复刻
add_吾导先路_复刻_resources(resource_stats)

# 落叶逐火
add_落叶逐火_resources(resource_stats)

# 登录活动
add_login_resources(resource_stats)

# 签到活动
add_check_in_resources(resource_stats)

# 幸运墙活动
add_lucky_wall_resources(resource_stats)

# 危机合约
# 起源行动
add_起源行动_resources(resource_stats)

# 引航者试炼
add_trials_for_navigator_resources(resource_stats)

# 生息演算
add_reclamation_algorithm_resources(resource_stats)

# 邮件
resource_stats.add("高级作战记录×5 应急理智加强剂×1 龙门币×16888",
                   "2023 - 新春会礼包（DAY1）",
                   "2023-01-15 04:00:00+08:00",  # 具体时间不明
                   "#2023 - 新春会礼包", "#兑换码免费领取")
resource_stats.add("应急理智加强剂×1 技巧概要·卷3×5 龙门币×16888",
                   "2023 - 新春会礼包（DAY2）",
                   "2023-01-16 04:00:00+08:00",  # 具体时间不明
                   "#2023 - 新春会礼包", "#兑换码免费领取")
resource_stats.add("应急理智加强剂×1 采购凭证×20 龙门币×16888",
                   "2023 - 新春会礼包（DAY3）",
                   "2023-01-17 04:00:00+08:00",  # 具体时间不明
                   "#2023 - 新春会礼包", "#兑换码免费领取")
resource_stats.add("龙门币×20000",
                   "2023 - 辞旧迎新：春种秋收 来自风笛的信息",
                   "2023-01-17 04:00:00+08:00",  # 具体时间不明
                   "#2023 - 辞旧迎新：春种秋收", "#兑换码免费领取")
# 2023 - 罗德岛鳞丸移动食坊 归类为 网页活动
resource_stats.add("摘自画卷的柿子×1 寻访凭证×1 轻锰矿×5",
                   "2023 - 辞旧迎新，除夕夜特别登录奖励 来自夕的祝福",
                   "2023-01-21 20:00:00+08:00",
                   "#2023 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("香脆桃酥饼×1 寻访凭证×1 白马醇×5",
                   "2023 - 辞旧迎新，除夕夜特别登录奖励 来自老鲤的祝福",
                   "2023-01-21 21:00:00+08:00",
                   "#2023 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("香辣火炉×1 寻访凭证×1 模组数据块×1",
                   "2023 - 辞旧迎新，除夕夜特别登录奖励 来自年的祝福",
                   "2023-01-21 22:00:00+08:00",
                   "#2023 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("金糖年糕×1 寻访凭证×1 芯片助剂×2",
                   "2023 - 辞旧迎新，除夕夜特别登录奖励 来自乌有的祝福",
                   "2023-01-21 23:00:00+08:00",
                   "#2023 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("合成玉×2100 木瓜叶馅饼×1 家具零件×2100 龙门币×2100",
                   "2023 - 辞旧迎新，除夕夜特别登录奖励 来自阿米娅的祝福",
                   "2023-01-22 00:00:00+08:00",
                   "#2023 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("龙门币×20000",
                   "2023 - 四周年庆典：糖果 来自伊芙利特的信息",
                   "2023-04-22 04:00:00+08:00",  # 具体时间不明
                   "#2023 - 四周年庆典：糖果", "#兑换码免费领取")
resource_stats.add("龙门币×20000",
                   "2023 - 夏日嘉年华：粉色棉花糖 来自桃金娘的信息",
                   "2023-07-23 04:00:00+08:00",  # 具体时间不明
                   "#2023 - 夏日嘉年华：粉色棉花糖", "#兑换码免费领取")
# 2023 - 软绵绵工坊 归类为 网页活动
resource_stats.add("龙门币×20000",
                   "2023 - 感谢庆典：演奏会贵宾 来自黑键的信息",
                   "2023-10-22 04:00:00+08:00",  # 具体时间不明
                   "#2023 - 感谢庆典：演奏会贵宾", "#兑换码免费领取")
# 2023 - 心灵之音 归类为 网页活动
resource_stats.add("龙门币×20000",
                   "2024 - 新春前瞻特辑：年宵花 来自林的信息",
                   "2024-01-27 04:00:00+08:00",  # 具体时间不明
                   "#2024 - 新春前瞻特辑：年宵花", "#兑换码免费领取")
resource_stats.add("应急理智浓缩液×2 高级作战记录×15 技巧概要·卷3×15 龙门币×36888",
                   "2024 - 新春会礼包",
                   "2024-01-28 04:00:00+08:00",  # 具体时间不明
                   "#2024 - 新春会礼包", "#兑换码免费领取")
resource_stats.add("纯净鲜花露×1 寻访凭证×1 全新装置×5",
                   "2024 - 辞旧迎新，除夕夜特别登录奖励 来自缪尔赛思的祝福",
                   "2024-02-09 20:00:00+08:00",
                   "#2024 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("火山熔岩蛋糕×1 寻访凭证×1 酮阵列×5",
                   "2024 - 辞旧迎新，除夕夜特别登录奖励 来自纯烬艾雅法拉的祝福",
                   "2024-02-09 21:00:00+08:00",
                   "#2024 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("午后田园茶点×1 寻访凭证×1 模组数据块×1",
                   "2024 - 辞旧迎新，除夕夜特别登录奖励 来自薇薇安娜的祝福",
                   "2024-02-09 22:00:00+08:00",
                   "#2024 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("脆壳糖油果×1 寻访凭证×1 芯片助剂×2",
                   "2024 - 辞旧迎新，除夕夜特别登录奖励 来自左乐的祝福",
                   "2024-02-09 23:00:00+08:00",
                   "#2024 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("合成玉×2100 奶油夹心饼干×1 家具零件×2100 龙门币×2100",
                   "2024 - 辞旧迎新，除夕夜特别登录奖励 来自阿米娅的祝福",
                   "2024-02-10 00:00:00+08:00",
                   "#2024 - 辞旧迎新，除夕夜特别登录奖励", "#游戏内邮件赠送")
resource_stats.add("龙门币×20000",
                   "2024 - 五周年庆典：花冠 来自阿米娅的信息",
                   "2024-04-29 04:00:00+08:00",  # 具体时间不明
                   "#2024 - 五周年庆典：花冠", "#兑换码免费领取")


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

resource_stats.add_tag("#剿灭作战", ["#剿灭作战首次通关", "#剿灭作战每周报酬"])
resource_stats.add_tag("#SideStory", ["SideStory首次通关", "SideStory赠送", "#SideStory商店", "SideStory物资箱"])
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
    result = resource_stats.query("2023-01-01 00:00:00+08:00", "2024-01-01 00:00:00+08:00", "#起源行动")
    for name, count in result:
        print(f"{name}: {count}")
    # print(resource_stats.tags)
