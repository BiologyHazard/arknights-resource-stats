from models import ResourceStats
from time_utils import CST
from triggers import CronTrigger, DateTrigger

from .manager import manager


@manager.register
def add_daily_weekly_monthly_resources(resource_stats: ResourceStats):
    # 理智自动回复
    # 假设每日 4 时回复 240 理智
    resource_stats.add("理智×240",
                       "理智自动回复",
                       CronTrigger(hour=4, timezone=CST),
                       "#理智自动回复")

    # 基建
    resource_stats.add(
        "基建日",
        "基建",
        CronTrigger(hour=4, timezone=CST),
        "#基建",
    )

    # 信用交易所
    resource_stats.add(
        "信用交易所日",
        "信用交易所",
        CronTrigger(hour=4, timezone=CST),
        "#信用交易所",
    )

    # 日常任务
    resource_stats.add(
        "龙门币×500 基础作战记录×3 龙门币×1000 技巧概要·卷1×2 招聘许可×1 基础作战记录×5 龙门币×2000 碳×3 加急许可×1 初级作战记录×5 合成玉×100 采购凭证×5 家具零件×60 PRTS剿灭代理卡×1 龙门币×6000 中级作战记录×6",
        "日常任务（三周年之后）（周一至周五）",
        CronTrigger(day_of_week="MON-FRI", hour=4, start_time="2022-05-02 04:00:00+08:00", timezone=CST),
        "#日常任务",
    )
    resource_stats.add(
        "龙门币×500 基础作战记录×3 龙门币×1000 技巧概要·卷1×2 招聘许可×1 基础作战记录×5 龙门币×2000 碳×3 招聘许可×1 初级作战记录×5 合成玉×100 采购凭证×5 家具零件×60 PRTS剿灭代理卡×1 龙门币×6000 中级作战记录×6",
        "日常任务（三周年之后）（周六至周日）",
        CronTrigger(day_of_week="SAT-SUN", hour=4, start_time="2022-05-02 04:00:00+08:00", timezone=CST),
        "#日常任务",
    )

    # 周常任务
    resource_stats.add(
        "龙门币×1000 基础作战记录×4 赤金×4 招聘许可×2 龙门币×2000 家具零件×50 初级作战记录×4 技巧概要·卷1×5 龙门币×4000 招聘许可×3 应急理智浓缩液×1 赤金×10 龙门币×6000 招聘许可×5 高级作战记录×4 家具零件×200 合成玉×500 采购凭证×30 资质凭证×20 应急理智浓缩液×1 中级作战记录×4 模组数据块×1 龙门币×10000 高级作战记录×5",
        "周常任务（三周年之后）",
        CronTrigger(day_of_week="MON", hour=4, start_time="2022-05-02 04:00:00+08:00", timezone=CST),
        "#周常任务",
    )

    # 剿灭作战每周报酬
    resource_stats.add(
        "理智扣除三星通关龙门币×-124 初级作战记录×49 合成玉×1800",
        "剿灭作战每周报酬",
        CronTrigger(day_of_week="MON", hour=4, start_time="2020-11-02 04:00:00+08:00", timezone=CST),
        "#剿灭作战每周报酬"
    )

    # 每月签到
    monthly_attendance_rewards = "龙门币×2000 基础作战记录×10 招聘许可×2 采购凭证×8 碳×5 技巧概要·卷1×5 赤金×6 龙门币×4000 初级作战记录×10 加急许可×2 资质凭证×10 家具零件×40 技巧概要·卷1×10 赤金×10 龙门币×6000 中级作战记录×6 寻访凭证×1 采购凭证×25 碳素×6 技巧概要·卷2×5 赤金×15 龙门币×8000 高级作战记录×4  招聘许可×3 高级凭证×5 家具零件×100 技巧概要·卷3×6 芯片助剂×1 龙门币×10000 高级作战记录×5 加急许可×3".split()
    for day_of_month, reward in enumerate(monthly_attendance_rewards, start=1):
        resource_stats.add(
            reward,
            f"每月{day_of_month}日签到",
            CronTrigger(day=day_of_month, hour=4, timezone=CST),
            "#每月签到"
        )

    # 资质凭证区
    resource_stats.add(
        "资质凭证×-2690 寻访凭证×2 招聘许可×15 合成玉×600 中级作战记录×60 龙门币×60000 赤金×120 家具零件×500 寻访凭证×2 招聘许可×20",
        "资质凭证区",
        CronTrigger(day=1, hour=4, start_time="2019-05-01 04:00:00+08:00", timezone=CST),
        "#资质凭证区",
    )

    # 采购凭证区
    resource_stats.add(
        "采购凭证×-480 模组数据块×4",
        "采购凭证区模组数据块",
        DateTrigger("2021-09-17 16:00:00+08:00")
        | CronTrigger(day=1, hour=4, start_time="2020-10-01 04:00:00+08:00", timezone=CST),
        "#采购凭证区",
    )

    # 保全派驻每月酬劳
    resource_stats.add(
        "数据增补条×60 数据增补仪×24",
        "保全派驻每月酬劳",
        DateTrigger("2022-12-15 16:00:00+08:00")
        | CronTrigger(day=16, hour=4, start_time="2023-01-16 04:00:00", timezone=CST),
        "#保全派驻酬劳",
    )
