from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

from models import ResourceStats
from time_utils import CST


def add_lucky_wall_resources(resource_stats: ResourceStats):
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2024-08 幸运墙登录活动',
        OrTrigger([
            DateTrigger('2024-08-01 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2024-08-02 04:00:00', end_date='2024-08-15 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2024-02 龙门幸运墙登录活动',
        OrTrigger([
            DateTrigger('2024-02-01 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2024-02-02 04:00:00', end_date='2024-02-15 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2023-08 龙门幸运墙登录活动',
        OrTrigger([
            DateTrigger('2023-08-01 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2023-08-02 04:00:00', end_date='2023-08-15 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2023-01 龙门幸运墙登录活动',
        OrTrigger([
            DateTrigger('2023-01-17 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2023-01-18 04:00:00', end_date='2023-01-31 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2022-08 际崖城惊奇墙登录活动',
        OrTrigger([
            DateTrigger('2022-08-11 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2022-08-12 04:00:00', end_date='2022-08-25 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2022-01 龙门幸运墙登录活动',
        OrTrigger([
            DateTrigger('2022-01-25 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2022-01-26 04:00:00', end_date='2022-02-08 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2021-08 双日城惊奇墙',
        OrTrigger([
            DateTrigger('2021-08-03 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2021-08-04 04:00:00', end_date='2021-08-17 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
    resource_stats.add(
        '合成玉×593.1521428571428',
        '2021-02 龙门幸运墙登录活动',
        OrTrigger([
            DateTrigger('2021-02-05 16:00:00', timezone=CST),
            CronTrigger(hour=4, start_date='2021-02-06 04:00:00', end_date='2021-02-19 04:00:00', timezone=CST),
        ]),
        '#幸运墙活动',
    )
