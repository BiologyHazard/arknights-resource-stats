from models import ResourceStats
from time_utils import CST
from triggers import DateTrigger, CronTrigger


def add_lucky_wall_resources(resource_stats: ResourceStats):
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2024-08 大巴扎许愿墙',
        DateTrigger('2024-08-01 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2024-08-02 04:00:00+08:00', end_time='2024-08-15 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2024-02 幸运墙登录活动',
        DateTrigger('2024-02-01 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2024-02-02 04:00:00+08:00', end_time='2024-02-15 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2023-08 汐斯塔涂鸦墙',
        DateTrigger('2023-08-01 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2023-08-02 04:00:00+08:00', end_time='2023-08-15 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2023-01 幸运墙登录活动',
        DateTrigger('2023-01-17 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2023-01-18 04:00:00+08:00', end_time='2023-01-31 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2022-08 惊奇墙登录活动',
        DateTrigger('2022-08-11 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2022-08-12 04:00:00+08:00', end_time='2022-08-25 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2022-01 幸运墙登录活动',
        DateTrigger('2022-01-25 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2022-01-26 04:00:00+08:00', end_time='2022-02-08 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2021-08 惊奇墙登录活动',
        DateTrigger('2021-08-03 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2021-08-04 04:00:00+08:00', end_time='2021-08-17 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2021-02 幸运墙登录活动',
        DateTrigger('2021-02-05 16:00:00+08:00')
        | CronTrigger(hour=4, start_time='2021-02-06 04:00:00+08:00', end_time='2021-02-19 04:00:00+08:00', timezone=CST),
        '#幸运墙活动',
    )
