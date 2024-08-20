from abc import ABC, abstractmethod
from collections.abc import Generator
from datetime import datetime, timedelta

from time_utils import DateTimeLike, to_aware_datetime


def less_than(a, b, can_equal: bool):
    if can_equal:
        return a <= b
    return a < b


class Trigger(ABC):
    """
    Abstract base class that defines the interface that every trigger must implement.
    """

    @abstractmethod
    def get_next_fire_time(self, time: DateTimeLike, inclusive: bool) -> datetime | None:
        raise NotImplementedError

    def iter_fire_time(self,
                       start_time: DateTimeLike,
                       end_time: DateTimeLike | None = None,
                       start_inclusive: bool = True,
                       end_inclusive: bool = False) -> Generator[datetime, None, None]:
        start_time = to_aware_datetime(start_time)
        if end_time is not None:
            end_time = to_aware_datetime(end_time)
        time: datetime | None = self.get_next_fire_time(start_time, start_inclusive)
        while time is not None and (end_time is None or less_than(time, end_time, end_inclusive)):
            yield time
            time = self.get_next_fire_time(time, False)

    def get_all_fire_time(self,
                          start_time: DateTimeLike,
                          end_time: DateTimeLike | None = None,
                          start_inclusive: bool = True,
                          end_inclusive: bool = False) -> list[datetime]:
        return list(self.iter_fire_time(start_time, end_time, start_inclusive, end_inclusive))

    def __or__(self, other) -> 'OrTrigger':
        return OrTrigger([self, other])


class OrTrigger(Trigger):
    def __init__(self, triggers: list[Trigger]):
        self.triggers: list[Trigger] = []
        for trigger in triggers:
            if isinstance(trigger, OrTrigger):
                self.triggers.extend(trigger.triggers)
            else:
                self.triggers.append(trigger)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.triggers!r})"

    def get_next_fire_time(self, time: DateTimeLike, inclusive: bool) -> datetime | None:
        fire_times = [trigger.get_next_fire_time(time, inclusive)
                      for trigger in self.triggers]
        fire_times = [fire_time for fire_time in fire_times if fire_time is not None]
        if fire_times:
            return min(fire_times)
        else:
            return None
