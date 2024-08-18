import json

with open(r"D:\BioHazard\Projects\github-clone\ArknightsGameData\zh_CN\gamedata\excel\item_table.json", "r", encoding="utf-8") as f:
    item_table = json.load(f)

for item in item_table["items"].values():
    name = item["name"]
    assert "×" not in name
