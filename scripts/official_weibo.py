import asyncio
import json
import re
from email.utils import parsedate_to_datetime
from pathlib import Path

import aiohttp
from bs4 import BeautifulSoup

json_api_url = "https://weibo.com/ajax/statuses/mymblog"
long_text_api_url = "https://weibo.com/ajax/statuses/longtext"
user_id = 6279793937
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "SINAGLOBAL=9115095640272.785.1698147413405; XSRF-TOKEN=-5lutA28axdYqWf1mjvsbm48; _s_tentry=my.sina.com.cn; UOR=,,my.sina.com.cn; Apache=1507541050052.932.1723885721006; ULV=1723885721033:2:1:1:1507541050052.932.1723885721006:1698147413408; ALF=1727086271; SUB=_2A25LzcHuDeRhGeFJ4lcX9CrMzjqIHXVoo1smrDV8PUJbkNAGLWj8kW1Nfq5HWVIqc0O7-tc37YM_-jm4fR9PzJXv; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhFB3am3OyHL6LCdD9KMrLP5JpX5KMhUgL.FoMN1K-cShB7SKq2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0.fSoBXeh-c; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; WBPSESS=vzN2IRbTfFdRiIdtr-mT_SRGVziwPOjWNImPCTuGPMkAifhQqmmEGHM-JQJI1iphpn0oAOlwsXzV4A9D6S36DH_k24ildDgJe24erSEg1_PVBijfaakH2JvIpWLJqhaKaMn7n5O_PZU6EGDorjC7AA==",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
}


async def request_and_save_json(page: int):
    print(f"Requesting page {page}")
    async with aiohttp.request("GET", json_api_url, params=dict(uid=str(user_id), page=str(page)), headers=headers) as response:
        obj = await response.json()
    with open(f"official_weibo/json/mymblog_uid={user_id}_page={page}.json", "w", encoding="utf-8") as fp:
        json.dump(obj, fp, ensure_ascii=False, indent=4)


async def request_and_save_longtext(id: str):
    print(f"Requesting id {id}")
    async with aiohttp.request("GET", long_text_api_url, params=dict(id=id), headers=headers) as response:
        obj = await response.json()
    with open(f"official_weibo/json/longtext_id={id}.json", "w", encoding="utf-8") as fp:
        json.dump(obj, fp, ensure_ascii=False, indent=4)


async def get_json_main():
    # tasks = []
    for page in range(0, 1):
        await request_and_save_json(page)
        await asyncio.sleep(2)
    #     tasks.append(request_and_save_json(page))
    # await asyncio.gather(*tasks)


async def get_long_text_main():
    for path in Path("official_weibo/json").iterdir():
        if path.is_file() and path.suffix == ".json" and path.name.startswith("mymblog"):
            with open(path, "r", encoding="utf-8") as fp:
                obj = json.load(fp)
            for item in obj["data"]["list"]:
                if item["isLongText"]:
                    id = item["mblogid"]
                    if not Path(f"official_weibo/json/longtext_id={id}.json").is_file():
                        await request_and_save_longtext(id)
                        await asyncio.sleep(2)


def get_info_main():
    data = []
    for path in Path("official_weibo/json").iterdir():
        if path.is_file() and path.suffix == ".json" and path.name.startswith("mymblog"):
            with open(path, "r", encoding="utf-8") as fp:
                obj = json.load(fp)
            for item in obj["data"]["list"]:
                id = item["id"]
                mblogid = item["mblogid"]
                created_at = item["created_at"]
                created_datetime = parsedate_to_datetime(created_at)
                if item["isLongText"]:
                    with open(f"official_weibo/json/longtext_id={mblogid}.json", "r", encoding="utf-8") as fp:
                        long_text_obj = json.load(fp)
                    try:
                        text = long_text_obj["data"]["longTextContent"]
                    except KeyError:
                        text = item["text_raw"]
                else:
                    text = item["text_raw"]

                data.append({
                    "id": id,
                    "url": f"https://weibo.com/{user_id}/{mblogid}",
                    "date": created_datetime.isoformat(" "),
                    "text": text,
                })
    data.sort(key=lambda x: x["date"])
    with open("official_weibo/weibo.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)
    # titles = [f"{x['date']} {x['category']} {x['heading']}" for x in data]
    # with open("official_websites/titles.txt", "w", encoding="utf-8") as fp:
    #     fp.write("\n".join(titles))


if __name__ == "__main__":
    # asyncio.run(get_json_main())
    # asyncio.run(get_long_text_main())
    get_info_main()
