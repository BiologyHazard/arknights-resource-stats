from models import ResourceStats
from triggers import DateTrigger, CronTrigger

from .manager import manager


@manager.register
def add_bilibili_live_mission_resources(resource_stats: ResourceStats):
    resource_stats.add(
        "龙门币×10000 龙门币×20000 高级作战记录×5",
        "明日方舟UP主应援计划 - 惊霆无声",
        DateTrigger("2023-04-06 16:00:00+08:00")
        | CronTrigger(hour=0, start_time="2023-04-07 00:00:00+08:00", end_time="2023-05-01 00:00:00+08:00"),
        "#bilibili直播任务",
    )
    resource_stats.add(
        "龙门币×10000 龙门币×20000 高级作战记录×5",
        "明日方舟UP主应援计划 - 眠于树影之中",
        DateTrigger("2023-07-06 16:00:00+08:00")
        | CronTrigger(hour=0, start_time="2023-07-07 00:00:00+08:00", end_time="2023-08-01 00:00:00+08:00"),
        "#bilibili直播任务",
    )
    resource_stats.add(
        "龙门币×10000 龙门币×20000 高级作战记录×5",
        "明日方舟UP主应援计划 - 晚冬特辑",
        DateTrigger("2023-12-28 16:00:00+08:00")
        | CronTrigger(hour=0, start_time="2023-12-29 00:00:00+08:00", end_time="2024-02-01 00:00:00+08:00"),
        "#bilibili直播任务",
    )
    resource_stats.add(
        "龙门币×10000 龙门币×20000 高级作战记录×5",
        "明日方舟UP主应援计划 - 怀黍离",
        DateTrigger("2024-02-01 16:00:00+08:00")
        | CronTrigger(hour=0, start_time="2024-02-02 00:00:00+08:00", end_time="2024-03-07 00:00:00+08:00"),
        "#bilibili直播任务",
    )
    resource_stats.add(
        "龙门币×10000 龙门币×20000 高级作战记录×5",
        "明日方舟UP主应援计划 - 熔炉还魂记",
        DateTrigger("2024-07-09 16:00:00+08:00")
        | CronTrigger(hour=0, start_time="2024-07-10 00:00:00+08:00", end_time="2024-08-01 00:00:00+08:00"),
        "#bilibili直播任务",
    )
