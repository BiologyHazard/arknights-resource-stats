import json

with open(r"D:\BioHazard\Projects\Others\森空岛\examples\GET https___zonai.skland.com_api_v1_game_attendance_uid=81827647.json", "r", encoding="utf-8") as fp:
    obj = json.load(fp)

skland_attendance_rewards = []

resource_info_map = obj["data"]["resourceInfoMap"]

for x in obj["data"]["calendar"]:
    print(f'II("{resource_info_map[x["resourceId"]]["name"]}", {x["count"]}),')
