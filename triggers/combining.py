from datetime import datetime

from time_utils import DateTimeLike, to_aware_datetime

from .trigger import Trigger


class CombiningTrigger(Trigger):
    __slots__ = ('triggers', 'jitter')

    def __init__(self, triggers: list[Trigger], jitter=None):
        self.triggers: list[Trigger] = triggers
        self.jitter = jitter

    def __repr__(self):
        if self.jitter:
            return f"{self.__class__.__name__}({self.triggers!r})"
        else:
            return f"{self.__class__.__name__}({self.triggers!r}, jitter={self.jitter!r})"


# class AndTrigger(CombiningTrigger):

#     __slots__ = ()

#     def get_next_fire_time(self, time: DateTimeLike, inclusive: bool = True) -> datetime | None:
#         while True:
#             fire_times = [trigger.get_next_fire_time(time, inclusive)
#                           for trigger in self.triggers]
#             if None in fire_times:
#                 return None
#             elif min(fire_times) == max(fire_times):  # type: ignore
#                 return fire_times[0]
#             else:
#                 time = max(fire_times)  # type: ignore


class OrTrigger(CombiningTrigger):

    __slots__ = ()

    def get_next_fire_time(self, time: DateTimeLike, inclusive: bool = True) -> datetime | None:
        fire_times = [trigger.get_next_fire_time(time)
                      for trigger in self.triggers]
        fire_times = [fire_time for fire_time in fire_times if fire_time is not None]
        if fire_times:
            return min(fire_times)
        else:
            return None
