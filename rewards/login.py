from apscheduler.triggers.date import DateTrigger

from models import ResourceStats
from time_utils import CST


def add_login_resources(resource_stats: ResourceStats):
    resource_stats.add(
        '璀璨闪耀寻访凭证×1',
        '2024-08 沉沙赫日登录活动',
        DateTrigger('2024-08-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '特勤专家寻访凭证×1',
        '2024-03 联动限时登录活动',
        DateTrigger('2024-03-07 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '时和岁丰寻访凭证×1',
        '2024-02 千秋一粟登录活动',
        DateTrigger('2024-02-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '烛照弦鸣寻访凭证×1',
        '2023-11 烛照弦鸣登录活动',
        DateTrigger('2023-11-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '龙门币×60000 合成玉×600 招聘许可×6 寒冬梦想放映机×1',
        '《明日方舟：冬隐归路》开播庆祝活动',
        DateTrigger('2023-10-06 04:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '云过天空寻访凭证×1',
        '2023-08 氤氲奇境登录活动',
        DateTrigger('2023-08-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '未来序曲寻访凭证×1',
        '2023-05 未来序曲登录活动',
        DateTrigger('2023-05-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '指引明路寻访凭证×1',
        '2023-03 砺火成锋登录活动',
        DateTrigger('2023-03-07 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '长风万里寻访凭证×1',
        '2023-01 万象伶仃登录活动',
        DateTrigger('2023-01-17 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '归狼踏影寻访凭证×1',
        '2022-11 归狼踏影登录活动',
        DateTrigger('2022-11-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '龙门币×60000 合成玉×600 招聘许可×6 希冀显影放映机×1',
        '《明日方舟：黎明前奏》开播纪念活动',
        DateTrigger('2022-10-28 04:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '淬火成诗寻访凭证×1',
        '2022-08 淬火成诗登录活动',
        DateTrigger('2022-08-11 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '晨雾灯塔寻访凭证×1',
        '2022-05 周年庆典登录活动',
        DateTrigger('2022-05-01 15:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '对酒当歌寻访凭证×1',
        '2022-01 浊酒澄心登录活动',
        DateTrigger('2022-01-25 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '唤曦炽焰寻访凭证×1',
        '2021-11 循光道途登录活动',
        DateTrigger('2021-11-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '乘风破浪寻访凭证×1',
        '2021-08 盛夏新星登录活动',
        DateTrigger('2021-08-03 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '幽海歌谣寻访凭证×1',
        '2021-05 周年庆典登录活动',
        DateTrigger('2021-05-01 15:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '特勤专家寻访凭证×1',
        '2021-03 联动限时登录活动',
        DateTrigger('2021-03-09 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '日落潮来寻访凭证×1',
        '2021-02 新春限时登录活动',
        DateTrigger('2021-02-05 16:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '只为铭记寻访凭证×1',
        '2020-11 感谢庆典登录活动',
        DateTrigger('2020-11-01 12:00:00', timezone=CST),
        '#登录活动',
    )
    resource_stats.add(
        '苏醒纪念寻访凭证×1',
        '2020-05 周年庆典登录活动',
        DateTrigger('2020-05-01 15:00:00', timezone=CST),
        '#登录活动',
    )
