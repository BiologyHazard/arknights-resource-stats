from collections.abc import Generator

from models import ItemInfoList
from scripts.excels import activity_table
from scripts.manager import Line, manager
from scripts.utils import get_event_name, get_reward_item_info_list


@manager.register(
    file_name="login",
    function_name="add_login_resources",
    import_str="""from models import ResourceStats

from .manager import manager""",
)
def login_only_rewards() -> Generator[Line, None, None]:
    assert ([event_id
             for event_id, event_basic_info in activity_table["basicInfo"].items()
             if event_basic_info["type"] == "LOGIN_ONLY"]
            == list(activity_table["activity"]["LOGIN_ONLY"]))
    for event_id in activity_table["activity"]["LOGIN_ONLY"]:
        event_basic_info = activity_table["basicInfo"][event_id]
        event_data = activity_table["activity"]["LOGIN_ONLY"][event_id]
        event_start_timestamp = event_basic_info["startTime"]
        event_name = get_event_name(event_id)

        item_info_list = ItemInfoList()
        for reward in event_data["itemList"]:
            item_info_list.extend(get_reward_item_info_list(reward))

        yield item_info_list, event_name, event_start_timestamp, ["#登录活动"], 6
