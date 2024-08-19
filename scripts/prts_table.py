import re
import sys
from datetime import datetime
from urllib.parse import quote

import mwparserfromhell as mw
import requests
from bs4 import BeautifulSoup
from mwparserfromhell.nodes.tag import Attribute, Tag
from mwparserfromhell.nodes.template import Parameter, Template
from mwparserfromhell.wikicode import Wikicode

sys.path.append(".")  # NOQA: E402
from models import ItemInfo, ItemInfoList
from scripts.event_start_time import event_start_time
from scripts.utils import get_event_id_by_name, get_furniture_id_by_name, furniture_to_intelligence_certificate


def get_edit_url(page_name: str) -> str:
    return f"https://prts.wiki/index.php?title={quote(page_name)}&action=edit"


def get_prts_source_code(url: str | bytes) -> str:
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    textarea = soup.find("textarea")
    source = textarea.get_text()  # type: ignore
    return source


def _get_event_shop_node(source: str) -> Template:
    wikicode: Wikicode = mw.parse(source)
    for node in wikicode.filter_templates(recursive=False):
        if node.name.strip_code() == "#invoke:EventShopList":
            return node
    else:
        raise ValueError("Activity shop not found")


def parse_event_shop(source: str, event_name: str) -> ItemInfoList:
    node = _get_event_shop_node(source)

    token_alias_parameter: Parameter = node.get("token_alias")  # type: ignore
    token_alias = token_alias_parameter.value.strip_code().strip().lstrip("带框_")
    data: Parameter = node.get("data")  # type: ignore
    value: Wikicode = data.value

    total_price = 0
    item_info_list = ItemInfoList()
    for line in value.splitlines():
        if not line:
            continue
        splitted = line.split(";;")
        if line.startswith("X"):  # stage header
            continue
            if len(splitted) == 3:
                _, stage_name, stage_color = splitted
            elif len(splitted) == 2:
                _, stage_name = splitted
                stage_color = None
            else:
                raise ValueError(f"Invalid line: {line}")

        elif line.startswith("0") or line.startswith("1"):  # item
            if len(splitted) == 5:
                checked, item_name, stock_count, unit_price, item_color = splitted
            elif len(splitted) == 4:
                checked, item_name, stock_count, unit_price = splitted
                item_color = None
            else:
                raise ValueError(f"Invalid line: {line}")

            if stock_count == "∞":
                continue  # skip infinite

            item_name: Wikicode = mw.parse(item_name)
            item_name_text = item_name.strip_code().strip().lstrip("link= ")
            if item_name_text.startswith("阶段商品"):
                item_name_text = item_name_text.split("：", 1)[1]
            if "专属时装 " in item_name_text:
                item_name_text = item_name_text.split("专属时装 ", 1)[1]

            stock_count = int(stock_count)
            unit_price = int(unit_price)
            name, unit_count = ItemInfo.new(item_name_text)
            count = unit_count * stock_count
            total_price += stock_count * unit_price
            if "图标 复刻转换.png" not in item_name:
                item_info_list.append_item_info(name, count)
            else:  # 复刻活动的家具，变成紫票
                event_id = get_event_id_by_name(event_name)
                furniture_id = get_furniture_id_by_name(name)
                assert unit_count == 1
                intelligence_certificate_count = furniture_to_intelligence_certificate(event_id, furniture_id) * count
                item_info_list.append_item_info("情报凭证", intelligence_certificate_count)

        else:  # comment or fold
            raise NotImplementedError(f"Unknown line: {line}")

    item_info_list.insert(0, ItemInfo(token_alias, -total_price))

    return item_info_list


def _get_intelligence_store_node(source: str) -> Tag:
    wikicode: Wikicode = mw.parse(source)
    for node in wikicode.filter_tags(recursive=False):
        attribute: Attribute = node.get("class")
        if attribute.value == "wikitable mw-collapsible mw-collapsed":
            return node
    else:
        raise ValueError("Intelligence store not found")


def parse_intelligence_store(source: str) -> list[tuple[str, ItemInfoList, int, datetime]]:
    table: Tag = _get_intelligence_store_node(source)

    activity_name_regex = r"\[\[.*?\|(.*?)\]\]"
    item_regex = r"\{\{道具图标\|(.+?)\|(\d+)?\|(?:\d+px)?\}\}×(\d+)"
    price_regex = r"\{\{价格\|情报凭证\|(\d+)\}\}"

    intelligence_store: list[tuple[str, ItemInfoList, int, datetime]] = []
    for line in table.contents.nodes[2:]:
        name_match = re.search(activity_name_regex, str(line))
        item_groups = re.findall(item_regex, str(line))
        price_match = re.search(price_regex, str(line))

        activity_name = name_match.group(1)  # type: ignore
        if activity_name == "理想城·复刻":
            activity_name = "理想城：长夏狂欢季·复刻"
        if activity_name == "玛莉娅·临光 复刻":
            activity_name = "玛莉娅·临光·复刻"
        start_time = event_start_time[activity_name]

        price = int(price_match.group(1))  # type: ignore

        item_info_list = ItemInfoList()
        for item_group in item_groups:
            item_name, unit_count, stock_count = item_group
            unit_count = int(unit_count) if unit_count else 1
            stock_count = int(stock_count)
            count = unit_count * stock_count
            item_info_list.append_item_info(item_name, count)

        intelligence_store.append((activity_name, item_info_list, price, start_time))

    return intelligence_store


def intelligence_store():
    url = "https://prts.wiki/index.php?title=%E9%87%87%E8%B4%AD%E4%B8%AD%E5%BF%83/%E5%87%AD%E8%AF%81%E4%BA%A4%E6%98%93%E6%89%80&action=edit&section=T-7"
    source = get_prts_source_code(url)
    intelligence_store = parse_intelligence_store(source)

    for activity_name, item_info_list, price, start_time in intelligence_store:
        s = f"""    resource_stats.add(
        "情报凭证×-{price} "
        "{item_info_list}",
        "{activity_name}情报凭证区",
        DateTrigger("{start_time}", timezone=CST),
        "#{activity_name}", "#情报凭证区",
    )"""
        print(s)


def _get_milestone_node(source: str) -> Template:
    wikicode: Wikicode = mw.parse(source)
    for node in wikicode.filter_templates(recursive=False):
        if node.name.strip_code() == "活动里程碑":
            return node
    else:
        raise ValueError("Milestone not found")


def parse_milestone(source: str, milestone_point_name: str) -> ItemInfoList:
    milestone_node: Template = _get_milestone_node(source)
    item_list = []
    i = 1
    while milestone_node.has(f"item{i}"):
        parameter: Parameter = milestone_node.get(f"item{i}")  # type: ignore
        item_list.append(parameter.value.strip().split(";;")[0])
        i += 1

    item_info_list = ItemInfoList()
    i = 1
    point = 0
    while milestone_node.has(str(i)):
        point = int(milestone_node.get(str(i)).value.strip_code().strip())  # type: ignore
        num = int(milestone_node.get(f"{i}num").value.strip_code().strip())  # type: ignore
        tp = int(milestone_node.get(f"{i}tp").value.strip_code().strip())  # type: ignore
        item_info_list.append_item_info(item_list[tp - 1], num)
        i += 1

    item_info_list.insert(0, ItemInfo(milestone_point_name, -point))
    return item_info_list


if __name__ == "__main__":
    # event_name = "将进酒2023"
    # event_name = "登临意"
    # event_name = "春分"
    event_name = "吾导先路2023"
    # event_name = "沙中之火"
    url = get_edit_url(event_name)
    source = get_prts_source_code(url)
    # print(parse_milestone(source, "繁荣证章"))
    print(parse_event_shop(source, event_name))
