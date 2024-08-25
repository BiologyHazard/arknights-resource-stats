import sys

sys.path.append(".")  # NOQA: E402

import json
import re
from datetime import date, datetime

from models import ItemInfoList
from scripts.generate_code import generate_file


def maintenance_rewards():
    with open("official_websites/news.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)
    for news in data:
        announcement_date = datetime.strptime(news["date"], "%Y // %m / %d").date()
        # Skip old news
        if announcement_date < date(2022, 12, 1):
            continue

        if (maintenance_type_match := re.search(r"闪断更新|停机维护", news["title"])) is not None:
            maintenance_type = maintenance_type_match.group()
            prefix_regex = r"(?:闪断更新|维护)时间：\s*"
            date_regex = r"(?P<year>\d{4})年(?P<month>\d{1,2})月(?P<day>\d{1,2})日"
            time_regex = r"(?:[上下]午)?(?P<hour>\d{2}):(?P<minute>\d{2})(?:\s*~\s*\d{2}:\d{2}\s*期间)?"
            datetime_regex = rf"{prefix_regex}{date_regex}{time_regex}"
            maintenance_datetime_match = re.search(datetime_regex, news["body"])
            assert maintenance_datetime_match is not None, news["body"]
            maintenance_datetime = datetime(**{k: int(v) for k, v in maintenance_datetime_match.groupdict().items()})  # type: ignore
            reward_match = re.search(r"补偿(?:内容)?：\s*(.*)\s*补偿范围", news["body"], re.DOTALL)
            assert reward_match is not None, news["body"]
            reward_str = reward_match.group(1)
            reward_items = re.findall(r"\s*(.+?)\s*[×\*]\s*(\d+)\s*、?\s*", reward_str)
            reward_items = [(name, int(count)) for name, count in reward_items]

            yield ItemInfoList.new(reward_items), f"{maintenance_datetime.strftime("%Y-%m-%d %H:%M")}{maintenance_type}补偿", maintenance_datetime, [f"#{maintenance_type}"], 1


if __name__ == "__main__":
    print(generate_file(
        maintenance_rewards,
        "add_maintenance_resources",
        """
from models import ResourceStats

from .manager import manager""",
    ))
