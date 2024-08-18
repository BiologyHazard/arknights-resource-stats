from apscheduler.triggers.date import DateTrigger

from models import ResourceStats
from time_utils import CST


def add_annihilation_first_clear_resources(resource_stats: ResourceStats):
    """不计理智消耗，不计合成玉报酬"""
    resource_stats.add(
        '资质凭证×4 初级作战记录×4 龙门币×4000 资质凭证×4 初级作战记录×6 龙门币×6000 资质凭证×8 初级作战记录×8 龙门币×8000 资质凭证×8 初级作战记录×10 龙门币×10000 高级凭证×4 中级作战记录×8 龙门币×15000 高级凭证×4 中级作战记录×10 龙门币×20000 高级凭证×8 中级作战记录×12 龙门币×25000 高级凭证×8 中级作战记录×15 龙门币×30000',
        '切尔诺伯格剿灭首次通关',
        DateTrigger('2019-04-30 10:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '资质凭证×5 初级作战记录×5 龙门币×5000 资质凭证×5 初级作战记录×8 龙门币×8000 资质凭证×10 初级作战记录×10 龙门币×10000 资质凭证×10 中级作战记录×8 龙门币×15000 高级凭证×5 中级作战记录×10 龙门币×20000 高级凭证×5 中级作战记录×12 龙门币×25000 高级凭证×10 中级作战记录×15 龙门币×30000 高级凭证×10 中级作战记录×20 龙门币×40000',
        '龙门外环剿灭首次通关',
        DateTrigger('2019-04-30 10:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '资质凭证×5 初级作战记录×5 龙门币×5000 资质凭证×5 初级作战记录×8 龙门币×8000 资质凭证×10 初级作战记录×10 龙门币×10000 资质凭证×10 中级作战记录×8 龙门币×15000 高级凭证×5 中级作战记录×10 龙门币×20000 高级凭证×5 中级作战记录×12 龙门币×25000 高级凭证×10 中级作战记录×15 龙门币×30000 高级凭证×10 中级作战记录×20 龙门币×40000',
        '龙门市区剿灭首次通关',
        DateTrigger('2019-07-22 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 固源岩组×3 合成玉×200 糖组×3 采购凭证×30 聚酸酯组×3 合成玉×300 异铁组×3 酮凝集组×3 采购凭证×40 全新装置×3 扭转醇×3 合成玉×400 三水锰矿×1 五水研磨石×1 采购凭证×60 芯片助剂×1 家具零件×100 合成玉×600 聚合剂×1 RMA70-24×1',
        '大骑士领郊外剿灭首次通关',
        DateTrigger('2020-11-02 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 凝胶×3 合成玉×200 炽合金×3 采购凭证×30 晶体元件×3 合成玉×300 固源岩组×3 糖组×3 采购凭证×40 聚酸酯组×3 异铁组×3 合成玉×400 酮阵列×1 改量装置×1 采购凭证×60 芯片助剂×1 家具零件×100 合成玉×600 聚合剂×1 白马醇×1',
        '北原冰封废城剿灭首次通关',
        DateTrigger('2021-01-04 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 轻锰矿×3 合成玉×200 研磨石×3 采购凭证×30 RMA70-12×3 合成玉×300 凝胶×3 炽合金×3 采购凭证×40 晶体元件×3 固源岩组×3 合成玉×400 糖聚块×1 聚酸酯块×1 采购凭证×60 芯片助剂×1 乌萨斯回声-废矿×1 合成玉×600 D32钢×1 异铁块×1',
        '废弃矿区剿灭首次通关',
        DateTrigger('2021-03-08 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 酮凝集组×3 合成玉×200 全新装置×3 采购凭证×30 扭转醇×3 合成玉×300 轻锰矿×3 研磨石×3 采购凭证×40 RMA70-12×3 凝胶×3 合成玉×400 炽合金块×1 晶体电路×1 采购凭证×60 芯片助剂×1 汐斯塔回声-海滨×1 合成玉×600 双极纳米片×1 提纯源岩×1',
        '潮没海滨剿灭首次通关',
        DateTrigger('2021-05-03 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 糖组×3 合成玉×200 聚酸酯组×3 采购凭证×30 异铁组×3 合成玉×300 酮凝集组×3 全新装置×3 采购凭证×40 扭转醇×3 轻锰矿×3 合成玉×400 五水研磨石×1 RMA70-24×1 采购凭证×60 芯片助剂×1 伊比利亚回声-潮窟×1 合成玉×600 双极纳米片×1 聚合凝胶×1',
        '积水潮窟剿灭首次通关',
        DateTrigger('2021-07-12 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 炽合金×3 合成玉×200 晶体元件×3 采购凭证×30 固源岩组×3 合成玉×300 糖组×3 聚酸酯组×3 采购凭证×40 异铁组×3 酮凝集组×3 合成玉×400 改量装置×1 白马醇×1 采购凭证×60 芯片助剂×1 萨尔贡回声-长泉×1 合成玉×600 双极纳米片×1 三水锰矿×1',
        '长泉镇郊野剿灭首次通关',
        DateTrigger('2021-09-06 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 研磨石×3 合成玉×200 RMA70-12×3 采购凭证×30 凝胶×3 合成玉×300 炽合金×3 晶体元件×3 采购凭证×40 固源岩组×3 糖组×3 合成玉×400 聚酸酯块×1 异铁块×1 采购凭证×60 芯片助剂×1 玻利瓦尔回声-换水口×1 合成玉×600 双极纳米片×1 酮阵列×1',
        '多索雷斯换水口剿灭首次通关',
        DateTrigger('2021-11-01 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 凝胶×3 合成玉×200 炽合金×3 采购凭证×30 化合切削液×3 合成玉×300 半自然溶剂×3 晶体元件×3 采购凭证×40 固源岩组×3 糖组×3 合成玉×400 聚酸酯块×1 异铁块×1 采购凭证×60 芯片助剂×1 哥伦比亚回声-监狱×1 合成玉×600 晶体电子单元×1 酮阵列×1',
        '南方监狱剿灭首次通关',
        DateTrigger('2022-01-10 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 半自然溶剂×3 合成玉×200 异铁组×3 采购凭证×30 酮凝集组×3 合成玉×300 全新装置×3 扭转醇×3 采购凭证×40 轻锰矿×3 研磨石×3 合成玉×400 RMA70-24×1 聚合凝胶×1 采购凭证×60 芯片助剂×1 维多利亚回声-小丘郡×1 合成玉×600 双极纳米片×1 炽合金块×1',
        '小丘郡郊野剿灭首次通关',
        DateTrigger('2022-03-07 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 晶体元件×3 合成玉×200 固源岩组×3 采购凭证×30 化合切削液×3 合成玉×300 半自然溶剂×3 异铁组×3 采购凭证×40 酮凝集组×3 全新装置×3 合成玉×400 白马醇×1 三水锰矿×1 采购凭证×60 芯片助剂×1 卡西米尔回声-竞技场×1 合成玉×600 D32钢×1 五水研磨石×1',
        '黑夜锦标秀剿灭首次通关',
        DateTrigger('2022-05-02 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 RMA70-12×3 合成玉×200 凝胶×3 采购凭证×30 炽合金×3 合成玉×300 晶体元件×3 固源岩组×3 采购凭证×40 化合切削液×3 半自然溶剂×3 合成玉×400 异铁块×1 酮阵列×1 采购凭证×60 芯片助剂×1 炎国回声-蜀道×1 合成玉×600 聚合剂×1 改量装置×1',
        '盘桓蜀道剿灭首次通关',
        DateTrigger('2022-07-11 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 扭转醇×3 合成玉×200 轻锰矿×3 采购凭证×30 研磨石×3 合成玉×300 RMA70-12×3 凝胶×3 采购凭证×40 炽合金×3 晶体元件×3 合成玉×400 提纯源岩×1 切削原液×1 采购凭证×60 芯片助剂×1 拉特兰回声-大街×1 合成玉×600 D32钢×1 精炼溶剂×1',
        '巧克力大街剿灭首次通关',
        DateTrigger('2022-09-05 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 转质盐组×3 合成玉×200 晶体元件×3 采购凭证×30 固源岩组×3 合成玉×300 化合切削液×3 半自然溶剂×3 采购凭证×40 异铁组×3 酮凝集组×3 合成玉×400 改量装置×1 白马醇×1 采购凭证×60 芯片助剂×1 伊比利亚回声-造船厂×1 合成玉×600 烧结核凝晶×1 三水锰矿×1',
        '昏黑造船厂剿灭首次通关',
        DateTrigger('2022-10-31 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 酮凝集组×3 合成玉×200 全新装置×3 采购凭证×30 扭转醇×3 合成玉×300 轻锰矿×3 研磨石×3 采购凭证×40 RMA70-12×3 凝胶×3 合成玉×400 炽合金块×1 转质盐聚块×1 采购凭证×60 芯片助剂×1 哥伦比亚回声-机库×1 合成玉×600 双极纳米片×1 晶体电路×1',
        '实验基地机库剿灭首次通关',
        DateTrigger('2023-01-09 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 固源岩组×3 合成玉×200 化合切削液×3 采购凭证×30 半自然溶剂×3 合成玉×300 异铁组×3 酮凝集组×3 采购凭证×40 全新装置×3 扭转醇×3 合成玉×400 三水锰矿×1 五水研磨石×1 采购凭证×60 芯片助剂×1 炎国龙门回声-商业街×1 合成玉×600 D32钢×1 RMA70-24×1',
        '龙门商业街剿灭首次通关',
        DateTrigger('2023-03-06 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 凝胶×3 合成玉×200 炽合金×3 采购凭证×30 转质盐组×3 合成玉×300 晶体元件×3 固源岩组×3 采购凭证×40 化合切削液×3 半自然溶剂×3 合成玉×400 异铁块×1 酮阵列×1 采购凭证×60 芯片助剂×1 莱塔尼亚回声-街道×1 合成玉×600 晶体电子单元×1 改量装置×1',
        '休止符街道剿灭首次通关',
        DateTrigger('2023-05-01 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 扭转醇×3 合成玉×200 轻锰矿×3 采购凭证×30 研磨石×3 合成玉×300 RMA70-12×3 凝胶×3 采购凭证×40 炽合金×3 转质盐组×3 合成玉×400 晶体电路×1 提纯源岩×1 采购凭证×60 芯片助剂×1 维多利亚回声-泥沼×1 合成玉×600 聚合剂×1 切削原液×1',
        '灰暗泥沼剿灭首次通关',
        DateTrigger('2023-07-10 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 半自然溶剂×3 合成玉×200 异铁组×3 采购凭证×30 酮凝集组×3 合成玉×300 全新装置×3 扭转醇×3 采购凭证×40 轻锰矿×3 研磨石×3 合成玉×400 RMA70-24×1 聚合凝胶×1 采购凭证×60 芯片助剂×1 萨尔贡回声-小水坑×1 合成玉×600 双极纳米片×1 炽合金块×1',
        '“特制小水坑”剿灭首次通关',
        DateTrigger('2023-09-04 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 转质盐组×3 合成玉×200 晶体元件×3 采购凭证×30 固源岩组×3 合成玉×300 化合切削液×3 半自然溶剂×3 采购凭证×40 异铁组×3 酮凝集组×3 合成玉×400 改量装置×1 白马醇×1 采购凭证×60 芯片助剂×1 维多利亚回声-荒野×1 合成玉×600 D32钢×1 三水锰矿×1',
        '腐烂荒野剿灭首次通关',
        DateTrigger('2023-10-30 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 转质盐组×3 合成玉×200 褐素纤维×3 采购凭证×30 环烃聚质×3 合成玉×300 晶体元件×3 固源岩组×3 采购凭证×40 化合切削液×3 半自然溶剂×3 合成玉×400 异铁块×1 酮阵列×1 采购凭证×60 芯片助剂×1 炎国回声-边城×1 合成玉×600 晶体电子单元×1 改量装置×1',
        '千嶂边城剿灭首次通关',
        DateTrigger('2024-01-08 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 扭转醇×3 合成玉×200 轻锰矿×3 采购凭证×30 研磨石×3 合成玉×300 RMA70-12×3 凝胶×3 采购凭证×40 炽合金×3 转质盐组×3 合成玉×400 固化纤维板×1 环烃预制体×1 采购凭证×60 芯片助剂×1 汐斯塔回声-大道×1 合成玉×600 烧结核凝晶×1 晶体电路×1',
        '新旅店大道剿灭首次通关',
        DateTrigger('2024-03-04 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 固源岩组×3 合成玉×200 化合切削液×3 采购凭证×30 半自然溶剂×3 合成玉×300 异铁组×3 酮凝集组×3 采购凭证×40 全新装置×3 扭转醇×3 合成玉×400 三水锰矿×1 五水研磨石×1 采购凭证×60 芯片助剂×1 哥伦比亚回声-实验室×1 合成玉×600 D32钢×1 RMA70-24×1',
        '“离心率”实验室剿灭首次通关',
        DateTrigger('2024-04-29 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
    resource_stats.add(
        '采购凭证×20 凝胶×3 合成玉×200 炽合金×3 采购凭证×30 转质盐组×3 合成玉×300 褐素纤维×3 环烃聚质×3 采购凭证×40 晶体元件×3 固源岩组×3 合成玉×400 切削原液×1 精炼溶剂×1 采购凭证×60 芯片助剂×1 维多利亚回声-街区×1 合成玉×600 聚合剂×1 异铁块×1',
        '燃烧街区剿灭首次通关',
        DateTrigger('2024-07-08 04:00:00', timezone=CST),
        '#剿灭作战首次通关',
    )
