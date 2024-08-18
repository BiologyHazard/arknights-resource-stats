from apscheduler.triggers.date import DateTrigger

from ..models import CST, ResourceStats


def add_将进酒复刻_resources(resource_stats: ResourceStats):
    resource_stats.add(
        "罐装晌午茶×-3110 "
        "阶段商品1：寒芒克洛丝的信物×1 阶段商品2：寒芒克洛丝的信物×1 阶段商品3：寒芒克洛丝的信物×1 阶段商品4：寒芒克洛丝的信物×1 阶段商品5：寒芒克洛丝的信物×1 寻访凭证×3 晶体电子单元×1 异铁块×3 白马醇×3 晶体电路×3 黄梨木方凳×4 透光竹帘×2 邀友遨游灯×2 壁间灯×4 RMA70-12×5 化合切削液×5 龙门币×100000 高级作战记录×10 中级作战记录×20 初级作战记录×40 技巧概要·卷3×10 技巧概要·卷2×20 聚酸酯×8 异铁×8 酮凝集×8 狙击芯片×5",
        "将进酒复刻活动商店",
        DateTrigger("2023-01-01 16:00:00", timezone=CST),
        "#将进酒复刻", "#活动商店",
    )
