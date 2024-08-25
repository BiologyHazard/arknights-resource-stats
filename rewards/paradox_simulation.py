from models import ResourceStats

from .manager import manager


@manager.register
def add_paradox_simulation_resources(resource_stats: ResourceStats):
    # 手动添加的部分
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '空弦、令、蚀清、暴雨悖论模拟', '2023-01-01 16:00:00+08:00', '#悖论模拟')

    # 由脚本自动生成的部分
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '星极、龙舌兰、深海色、罗比菈塔悖论模拟', '2022-12-01 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '琴柳、梅、慕斯悖论模拟', '2022-12-15 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '夕、阿、老鲤、桑葚悖论模拟', '2023-01-17 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '夜半、夏栎、爱丽丝、贾维悖论模拟', '2023-02-14 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200',
                       '菲亚梅塔悖论模拟', '2023-02-21 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '鸿雪、月禾、雪雉、酸糖悖论模拟', '2023-03-07 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '拜松、巫恋、鞭刃悖论模拟', '2023-03-21 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200',
                       '卡达悖论模拟', '2023-04-06 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '流明、断崖、莱恩哈特、石英悖论模拟', '2023-04-20 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '多萝西、明椒、慑砂、格劳克斯、霜叶悖论模拟', '2023-05-01 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '埃拉托、晓歌、风丸、杰克悖论模拟', '2023-05-22 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '送葬人、见行者、惊蛰悖论模拟', '2023-06-08 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '黑键、濯尘芙蓉、火哨、卡夫卡、布丁、宴悖论模拟', '2023-06-20 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '缪尔赛思、雪绒、但书、赤冬悖论模拟', '2023-07-06 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '星源、承曦格雷伊、蛇屠箱、夜刀悖论模拟', '2023-07-18 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200',
                       '桃金娘、休谟斯悖论模拟', '2023-08-01 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '百炼嘉维尔、至简、格拉尼、褐果、芙蓉悖论模拟', '2023-08-31 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '圣约送葬人、羽毛笔、清流悖论模拟', '2023-09-05 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '号角、达格达、贝娜、红云、铅踝悖论模拟', '2023-09-27 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '苇草、海蒂、杏仁悖论模拟', '2023-10-08 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '早露、伺夜、车尔尼、寒檀、暮落悖论模拟', '2023-11-01 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '灵知、耶拉、和弦悖论模拟', '2023-12-05 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '青枳、安赛尔、泡泡、玫拉悖论模拟', '2024-01-09 16:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '重岳、仇白、铎铃悖论模拟', '2024-02-01 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '艾丽妮、斥罪、空构、子月、摩根、维荻悖论模拟', '2024-04-11 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '阿斯卡纶、闪灵、推进之王、归溟幽灵鲨、阿罗玛、灰喉悖论模拟', '2024-05-01 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200',
                       '冰酿、隐现、露托悖论模拟', '2024-06-05 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '哈洛德、温米、安比尔、跃跃悖论模拟', '2024-07-09 10:00:00+08:00', '#悖论模拟')
    resource_stats.add('合成玉×200 合成玉×200 合成玉×200 合成玉×200 合成玉×200',
                       '纯烬艾雅法拉、泥岩、谜图、洋灰、苍苔悖论模拟', '2024-08-01 10:00:00+08:00', '#悖论模拟')
