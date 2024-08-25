import asyncio
import json
import re
from pathlib import Path

import aiohttp
from bs4 import BeautifulSoup

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"

news_api_url = "https://ak.hypergryph.com/api/news"  # ?category={category}&page={page}
news_url = "https://ak.hypergryph.com/news/{cid}"

categories = ["LATEST", "ANNOUNCEMENT", "ACTIVITY", "NEWS"]
max_pages = [2, 125, 27, 9]


async def request_and_save_json(category: str, page: int):
    print(f"Requesting {category} page {page}")
    async with aiohttp.request("GET", news_api_url, params=dict(category=category, page=str(page))) as response:
        obj = await response.json()
    with open(f"official_websites/json/{category}_{page}.json", "w", encoding="utf-8") as fp:
        json.dump(obj, fp, ensure_ascii=False, indent=4)


async def request_and_save_page(cid: str):
    print(f"Requesting cid {cid}")
    async with aiohttp.request("GET", news_url.format(cid=cid)) as response:
        content = await response.read()
    with open(f"official_websites/html/news_{cid}.html", "wb") as fp:
        fp.write(content)


async def get_json_main():
    tasks = []
    for category, max_page in zip(categories, max_pages):
        for page in range(1, max_page + 1):
            tasks.append(request_and_save_json(category, page))
    await asyncio.gather(*tasks)


async def get_page_main():
    tasks = []
    for category, max_page in zip(categories, max_pages):
        for page in range(1, max_page + 1):
            with open(f"official_websites/json/{category}_{page}.json", "r", encoding="utf-8") as fp:
                obj = json.load(fp)
            for news in obj["data"]["list"]:
                cid = news["cid"]
                if Path(f"official_websites/html/news_{cid}.html").exists():
                    continue
                tasks.append(request_and_save_page(cid))
    await asyncio.gather(*tasks)


def get_info_main():
    data = []
    for path in Path("official_websites/html").iterdir():
        if path.is_file() and path.suffix == ".html":
            cid = path.stem.split("_")[1]
            url = news_url.format(cid=cid)
            with open(path, "r", encoding="utf-8") as fp:
                soup = BeautifulSoup(fp, "html.parser")
            date_div = soup.find("div", class_="_8f259902")
            date_text = date_div.get_text(strip=True)  # type: ignore
            category_div = soup.find("div", class_="_0edddcb6")
            category_text = category_div.get_text(strip=True)  # type: ignore
            title_div = soup.find("div", class_="_86483275")
            title_text = title_div.get_text(strip=True)  # type: ignore
            body_div = soup.find("div", class_="_0868052a")
            for br_tag in body_div.find_all("br"):  # type: ignore
                br_tag.replace_with("\n")
            body_text = body_div.get_text()  # type: ignore
            images = body_div.find_all("img")  # type: ignore
            images = [img["src"] for img in images]
            data.append({
                "cid": cid,
                "url": url,
                "date": date_text,
                "category": category_text,
                "title": title_text,
                "body": body_text,
                "images": images
            })
    data.sort(key=lambda x: x["date"])
    with open("official_websites/news.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)
    # titles = [f"{x['date']} {x['category']} {x['heading']}" for x in data]
    # with open("official_websites/titles.txt", "w", encoding="utf-8") as fp:
    #     fp.write("\n".join(titles))


def is_封禁处理公示(news):
    return "封禁处理公示" in news["title"]


def is_闪断更新公告(news):
    return "闪断更新" in news["title"]


def is_临时不停机更新公告(news):
    return "不停机更新" in news["title"]


def is_停机维护(news):
    return "停机维护" in news["title"]


def is_制作组通讯(news):
    return "制作组通讯" in news["title"]


def is_未成年人游戏限时通知(news):
    return "未成年人游戏限时通知" in news["title"]


def is_公开招募标签强制刷新通知(news):
    return "【公开招募】标签强制刷新通知" in news["title"]


def is_新闻(news):
    return news["category"] == "新闻"


def is_活动(news):
    return news["category"] == "活动"


def arrange_titles():
    with open("official_websites/news.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)

    data.sort(key=lambda x: (
        is_封禁处理公示(x),
        is_闪断更新公告(x),
        is_临时不停机更新公告(x),
        is_停机维护(x),
        is_制作组通讯(x),
        is_未成年人游戏限时通知(x),
        is_公开招募标签强制刷新通知(x),
        is_新闻(x),
        is_活动(x),
    ))
    titles = [f"{x['date']} {x['category']} {x['title']}" for x in data]
    with open("official_websites/titles.txt", "w", encoding="utf-8") as fp:
        fp.write("\n".join(titles))


def get_闪断更新补偿():
    with open("official_websites/news.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)
    for news in data:
        body: str = news["body"].replace("\n", "")
        # matches = list(re.finditer(r"补偿(?!范围)", body))
        matches = list(re.finditer(r"邮件", body))
        for match in matches:
            index = match.start()
            text = body[index:index+20]
            print(text)


if __name__ == "__main__":
    # asyncio.run(get_json_main())
    # asyncio.run(get_page_main())
    # get_info_main()
    arrange_titles()
    # get_闪断更新补偿()
