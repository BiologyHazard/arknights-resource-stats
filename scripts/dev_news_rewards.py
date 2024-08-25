import json
import re
from datetime import datetime

from scripts.manager import manager
from models import ItemInfoList


@manager.register(
    "dev_news",
    "add_dev_news_rewards",
    """
from models import ResourceStats

from .manager import manager"""
)
def dev_news_rewards():
    with open("official_websites/news.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)
    for news in data:
        if "制作组通讯" not in news["title"]:
            continue
        index_match = re.search(r"#(\d+)", news["title"])
        reward_match = re.search(r"合成玉\s*\*\s*200\s*、?(.+?)\s*\*\s*5", news["body"])
        date_match = re.search(r"发放时间：(?P<month>\d+)月(?P<day>\d+)日(?P<hour>\d+):(?P<minute>\d+)", news["body"])
        assert index_match is not None, news["title"]
        assert reward_match is not None, news["body"]
        assert date_match is not None, news["body"]
        index = int(index_match.group(1))
        reward = reward_match.group(1)
        date_obj = datetime.strptime(news["date"], "%Y // %m / %d").date()
        assert date_obj.month == int(date_match.group("month"))
        assert date_obj.day == int(date_match.group("day"))
        datetime_obj = datetime(date_obj.year, date_obj.month, date_obj.day,
                                int(date_match.group("hour")), int(date_match.group("minute")))
        yield ItemInfoList.new(f"合成玉×200 {reward}×5"), f"制作组通讯#{index}", datetime_obj, ["#制作组通讯"], 2
