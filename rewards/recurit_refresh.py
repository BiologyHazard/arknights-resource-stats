from models import ResourceStats

from .manager import manager


@manager.register
def add_recurit_refresh_resources(resource_stats: ResourceStats):
    resource_stats.add("公开招募刷新×2",
                       "2023春节公开招募刷新", "2023-01-17 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "2023春节公开招募刷新补偿", "2023-01-17 16:00:00+08:00", "#公开招募刷新", "#邮件")
    resource_stats.add("公开招募刷新×2",
                       "四周年庆典Part1公开招募刷新", "2023-05-01 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "四周年庆典Part1公开招募刷新补偿", "2023-05-01 16:00:00+08:00", "#公开招募刷新", "#邮件")
    resource_stats.add("公开招募刷新×2",
                       "四周年庆典Part2公开招募刷新", "2023-05-22 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "四周年庆典Part2公开招募刷新补偿", "2023-05-22 16:00:00+08:00", "#公开招募刷新", "#邮件")
    resource_stats.add("公开招募刷新×2",
                       "2023夏日嘉年华公开招募刷新", "2023-08-01 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "2023夏日嘉年华公开招募刷新补偿", "2023-08-01 16:00:00+08:00", "#公开招募刷新", "#邮件")
    resource_stats.add("公开招募刷新×2",
                       "2023感谢庆典公开招募刷新", "2023-11-01 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "2023感谢庆典公开招募刷新补偿", "2023-11-01 16:00:00+08:00", "#公开招募刷新", "#邮件")
    resource_stats.add("公开招募刷新×2",
                       "2024春节公开招募刷新", "2024-02-01 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "2024春节公开招募刷新补偿", "2024-02-01 16:00:00+08:00", "#公开招募刷新", "#邮件")
    resource_stats.add("公开招募刷新×2",
                       "五周年庆典公开招募刷新", "2024-05-01 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "五周年庆典公开招募刷新补偿", "2024-05-01 16:00:00+08:00", "#公开招募刷新", "#邮件")
    resource_stats.add("公开招募刷新×2",
                       "2024夏日嘉年华公开招募刷新", "2024-08-01 16:00:00+08:00", "#公开招募刷新")
    resource_stats.add("招聘许可×5 加急许可×5",
                       "2024夏日嘉年华公开招募刷新补偿", "2024-08-01 16:00:00+08:00", "#公开招募刷新", "#邮件")
