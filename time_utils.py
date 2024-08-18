from datetime import datetime, timedelta, timezone


CST = timezone(timedelta(hours=8), "中国标准时间")
DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

type DateTimeLike = datetime | str | int | float


def get_CST_datetime(dt: DateTimeLike, format: str = DEFAULT_TIME_FORMAT) -> datetime:
    if isinstance(dt, (int, float)):
        return datetime.fromtimestamp(dt, CST)
    if isinstance(dt, str):
        return datetime.strptime(dt, format).replace(tzinfo=CST)
    return dt.astimezone(CST)


def get_CST_time_str(dt: DateTimeLike, format: str = DEFAULT_TIME_FORMAT) -> str:
    return get_CST_datetime(dt).strftime(format)
