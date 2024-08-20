from datetime import datetime, timedelta, timezone, tzinfo


CST = timezone(timedelta(hours=8), "中国标准时间")
DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

type DateTimeLike = datetime | str | int | float


def to_datetime(dt: DateTimeLike) -> datetime:
    if isinstance(dt, (int, float)):
        return datetime.fromtimestamp(dt).astimezone()
    elif isinstance(dt, str):
        return datetime.fromisoformat(dt)
    return dt


def to_aware_datetime(dt: DateTimeLike) -> datetime:
    dt = to_datetime(dt)
    if dt.tzinfo is None:
        dt = dt.astimezone()
    return dt


def to_CST_datetime(dt: DateTimeLike) -> datetime:
    if isinstance(dt, (int, float)):
        return datetime.fromtimestamp(dt, CST)
    elif isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=CST)
    else:
        return dt.astimezone(CST)


def to_CST_time_str(dt: DateTimeLike) -> str:
    return to_CST_datetime(dt).isoformat(" ")
