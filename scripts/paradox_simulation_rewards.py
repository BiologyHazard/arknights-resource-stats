import sys

sys.path.append(".")  # NOQA: E402

import json
import re
from datetime import date, datetime

from models import ItemInfoList
from scripts.generate_code import generate_file


def paradox_simulation_rewards():
    with open("official_websites/news.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)
    for news in data:
        announcement_date = datetime.strptime(news["date"], "%Y // %m / %d").date()
        # Skip old news
        if announcement_date < date(2022, 12, 1):
            continue

        if "悖论模拟" in news["body"]:
            prefix_regex = r"(?:闪断更新|维护)时间：\s*"
            date_regex = r"(?P<year>\d{4})年(?P<month>\d{1,2})月(?P<day>\d{1,2})日"
            time_regex = r"(?:[上下]午)?(?P<hour>\d{2}):(?P<minute>\d{2})(?:\s*~\s*\d{2}:\d{2}\s*期间)?"
            datetime_regex = rf"{prefix_regex}{date_regex}{time_regex}"
            maintenance_datetime_match = re.search(datetime_regex, news["body"])
            assert maintenance_datetime_match is not None, news["body"]
            maintenance_datetime = datetime(**{k: int(v) for k, v in maintenance_datetime_match.groupdict().items()})  # type: ignore

            paradox_match = re.search(r"新增以下干员的【悖论模拟】：(【.+?】(?:、【.+?】)*)◆", news["body"])
            if paradox_match is None:
                continue
            operator_names = re.findall(r"【(.+?)】", paradox_match.group(1))
            yield ItemInfoList.new(["合成玉×200"] * len(operator_names)), f"{"、".join(operator_names)}悖论模拟", maintenance_datetime, ["#悖论模拟"], 2


if __name__ == "__main__":
    print(generate_file(
        paradox_simulation_rewards,
        "add_paradox_simulation_resources",
        """
from models import ResourceStats

from .manager import manager""",
    ))
