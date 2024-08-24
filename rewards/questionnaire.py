from models import ResourceStats

from .manager import manager


@manager.register
def add_questionnaire_rewards(resource_stats: ResourceStats):
    resource_stats.add(
        "合成玉×600",
        "生息演算沙中之火问卷",
        "2023-02-17 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×600",
        "四周年问卷",
        "2023-05-11 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×300",
        "尖灭测试作战问卷",
        "2023-06-01 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×300",
        "探索者的银凇止境问卷",
        "2023-09-01 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×300",
        "纷争演绎问卷",
        "2023-10-07 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×600",
        "2023感谢庆典调研问卷",
        "2023-11-17 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×300",
        "浊燃作战问卷",
        "2023-12-04 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×300",
        "生息演算沙洲遗闻问卷",
        "2024-02-09 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×600",
        "五周年庆典问卷",
        "2024-05-10 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×300",
        "促融共竞问卷",
        "2024-05-25 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
    resource_stats.add(
        "合成玉×300",
        "萨卡兹的无终奇语问卷",
        "2024-07-24 04:00:00+08:00",  # 具体时间不明
        "#问卷",
    )
