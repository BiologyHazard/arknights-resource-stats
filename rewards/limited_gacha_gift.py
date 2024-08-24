from models import ResourceStats
from triggers import CronTrigger, DateTrigger
from time_utils import CST

from .manager import manager


@manager.register
def add_limited_gacha_gift_resources(resource_stats: ResourceStats):
    resource_stats.add(
        "【万象伶仃】限定寻访",
        "【万象伶仃】限定寻访每日赠送",
        DateTrigger("2023-01-17 16:00:00+08:00")
        | CronTrigger(hour=4, start_time="2023-01-18 04:00:00+08:00", end_time="2023-01-31 04:00:00+08:00", timezone=CST),
        "#限定寻访每日赠送",
    )
    resource_stats.add(
        "【真理孑然】限定寻访",
        "【真理孑然】限定寻访每日赠送",
        DateTrigger("2023-05-01 16:00:00+08:00")
        | CronTrigger(hour=4, start_time="2023-05-02 04:00:00+08:00", end_time="2023-05-15 04:00:00+08:00", timezone=CST),
        "#限定寻访每日赠送",
    )
    resource_stats.add(
        "【云间清醒梦】限定寻访",
        "【云间清醒梦】限定寻访每日赠送",
        DateTrigger("2023-08-01 16:00:00+08:00")
        | CronTrigger(hour=4, start_time="2023-08-02 04:00:00+08:00", end_time="2023-08-15 04:00:00+08:00", timezone=CST),
        "#限定寻访每日赠送",
    )
    resource_stats.add(
        "【宿愿】限定寻访",
        "【宿愿】限定寻访每日赠送",
        DateTrigger("2023-11-01 16:00:00+08:00")
        | CronTrigger(hour=4, start_time="2023-11-02 04:00:00+08:00", end_time="2023-11-15 04:00:00+08:00", timezone=CST),
        "#限定寻访每日赠送",
    )
    resource_stats.add(
        "【千秋一粟】限定寻访",
        "【千秋一粟】限定寻访每日赠送",
        DateTrigger("2024-02-01 16:00:00+08:00")
        | CronTrigger(hour=4, start_time="2024-02-02 04:00:00+08:00", end_time="2024-02-15 04:00:00+08:00", timezone=CST),
        "#限定寻访每日赠送",
    )
    resource_stats.add(
        "【何以为我】限定寻访",
        "【何以为我】限定寻访每日赠送",
        DateTrigger("2024-05-01 16:00:00+08:00")
        | CronTrigger(hour=4, start_time="2024-05-02 04:00:00+08:00", end_time="2024-05-15 04:00:00+08:00", timezone=CST),
        "#限定寻访每日赠送",
    )
    resource_stats.add(
        "【在流沙上刻印】限定寻访",
        "【在流沙上刻印】限定寻访每日赠送",
        DateTrigger("2024-08-01 16:00:00+08:00")
        | CronTrigger(hour=4, start_time="2024-08-02 04:00:00+08:00", end_time="2024-08-15 04:00:00+08:00", timezone=CST),
        "#限定寻访每日赠送",
    )
