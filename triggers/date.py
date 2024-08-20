from datetime import datetime

from time_utils import DateTimeLike, to_aware_datetime

from .trigger import Trigger, less_than


class DateTrigger(Trigger):
    __slots__ = 'time'

    def __init__(self, time: DateTimeLike):
        self.time = to_aware_datetime(time)

    def get_next_fire_time(self, time: DateTimeLike, inclusive: bool) -> datetime | None:
        time = to_aware_datetime(time)
        if less_than(time, self.time, inclusive):
            return self.time
        else:
            return None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.time.isoformat(" "))})"
