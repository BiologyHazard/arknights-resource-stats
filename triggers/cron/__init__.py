from datetime import datetime, timedelta, tzinfo
from typing import ClassVar

from tzlocal import get_localzone

from time_utils import DateTimeLike, to_aware_datetime

from ..trigger import Trigger
from .fields import DEFAULT_VALUES, BaseField, DayOfMonthField, DayOfWeekField, MonthField, WeekField
from .util import datetime_ceil, localize, normalize


class CronTrigger(Trigger):
    FIELD_NAMES: ClassVar[tuple[str, ...]] = ('year', 'month', 'day', 'week', 'day_of_week', 'hour', 'minute', 'second')
    FIELDS_MAP: ClassVar[dict[str, type[BaseField]]] = {
        'year': BaseField,
        'month': MonthField,
        'week': WeekField,
        'day': DayOfMonthField,
        'day_of_week': DayOfWeekField,
        'hour': BaseField,
        'minute': BaseField,
        'second': BaseField
    }

    __slots__ = 'timezone', 'start_time', 'end_time', 'fields'

    def __init__(self,
                 year: int | str | None = None,
                 month: int | str | None = None,
                 day: int | str | None = None,
                 week: int | str | None = None,
                 day_of_week: int | str | None = None,
                 hour: int | str | None = None,
                 minute: int | str | None = None,
                 second: int | str | None = None,
                 start_time: DateTimeLike | None = None,
                 end_time: DateTimeLike | None = None,
                 timezone: tzinfo | None = None):
        if timezone:
            self.timezone = timezone
        elif isinstance(start_time, datetime) and start_time.tzinfo:
            self.timezone = start_time.tzinfo
        elif isinstance(end_time, datetime) and end_time.tzinfo:
            self.timezone = end_time.tzinfo
        else:
            self.timezone = get_localzone()

        # self.start_date = convert_to_datetime(start_date, self.timezone, 'start_date')
        # self.end_date = convert_to_datetime(end_date, self.timezone, 'end_date')
        self.start_time = to_aware_datetime(start_time) if start_time else None
        self.end_time = to_aware_datetime(end_time) if end_time else None

        values = dict((key, value) for (key, value) in locals().items()
                      if key in self.FIELD_NAMES and value is not None)
        self.fields: list[BaseField] = []
        assign_defaults = False
        for field_name in self.FIELD_NAMES:
            if field_name in values:
                exprs = values.pop(field_name)
                is_default = False
                assign_defaults = not values
            elif assign_defaults:
                exprs = DEFAULT_VALUES[field_name]
                is_default = True
            else:
                exprs = '*'
                is_default = True

            field_class = self.FIELDS_MAP[field_name]
            field = field_class(field_name, exprs, is_default)
            self.fields.append(field)

    @classmethod
    def from_crontab(cls, expr, timezone=None):
        """
        Create a :class:`~CronTrigger` from a standard crontab expression.

        See https://en.wikipedia.org/wiki/Cron for more information on the format accepted here.

        :param expr: minute, hour, day of month, month, day of week
        :param datetime.tzinfo|str timezone: time zone to use for the date/time calculations (
            defaults to scheduler timezone)
        :return: a :class:`~CronTrigger` instance

        """
        values = expr.split()
        if len(values) != 5:
            raise ValueError('Wrong number of fields; got {}, expected 5'.format(len(values)))

        return cls(minute=values[0],
                   hour=values[1],
                   day=values[2],
                   month=values[3],
                   day_of_week=values[4],
                   timezone=timezone)

    def _increment_field_value(self, dateval, fieldnum):
        """
        Increments the designated field and resets all less significant fields to their minimum
        values.

        :type dateval: datetime
        :type fieldnum: int
        :return: a tuple containing the new date, and the number of the field that was actually
            incremented
        :rtype: tuple
        """

        values = {}
        i = 0
        while i < len(self.fields):
            field = self.fields[i]
            if not field.REAL:
                if i == fieldnum:
                    fieldnum -= 1
                    i -= 1
                else:
                    i += 1
                continue

            if i < fieldnum:
                values[field.name] = field.get_value(dateval)
                i += 1
            elif i > fieldnum:
                values[field.name] = field.get_min(dateval)
                i += 1
            else:
                value = field.get_value(dateval)
                maxval = field.get_max(dateval)
                if value == maxval:
                    fieldnum -= 1
                    i -= 1
                else:
                    values[field.name] = value + 1
                    i += 1

        difference = datetime(**values) - dateval.replace(tzinfo=None)
        return normalize(dateval + difference), fieldnum

    def _set_field_value(self, dateval, fieldnum, new_value):
        values = {}
        for i, field in enumerate(self.fields):
            if field.REAL:
                if i < fieldnum:
                    values[field.name] = field.get_value(dateval)
                elif i > fieldnum:
                    values[field.name] = field.get_min(dateval)
                else:
                    values[field.name] = new_value

        return localize(datetime(**values), self.timezone)

    def get_next_fire_time(self, time: DateTimeLike, inclusive: bool):
        time = to_aware_datetime(time)
        if not inclusive:
            time += timedelta.resolution
        start_date = max(time, self.start_time) if self.start_time else time

        fieldnum = 0
        next_time = datetime_ceil(start_date).astimezone(self.timezone)
        while 0 <= fieldnum < len(self.fields):
            field = self.fields[fieldnum]
            curr_value = field.get_value(next_time)
            next_value = field.get_next_value(next_time)

            if next_value is None:
                # No valid value was found
                next_time, fieldnum = self._increment_field_value(next_time, fieldnum - 1)
            elif next_value > curr_value:
                # A valid, but higher than the starting value, was found
                if field.REAL:
                    next_time = self._set_field_value(next_time, fieldnum, next_value)
                    fieldnum += 1
                else:
                    next_time, fieldnum = self._increment_field_value(next_time, fieldnum)
            else:
                # A valid value was found, no changes necessary
                fieldnum += 1

            # Return if the date has rolled past the end date
            if self.end_time and next_time >= self.end_time:
                return None

        if fieldnum >= 0:
            return min(next_time, self.end_time) if self.end_time else next_time

    def __repr__(self):
        options = ["%s='%s'" % (f.name, f) for f in self.fields if not f.is_default]
        if self.start_time:
            options.append(f"start_date={repr(self.start_time.isoformat(" "))}")
        if self.end_time:
            options.append(f"end_date={repr(self.end_time.isoformat(" "))}")

        return "%s(%s, timezone='%s')" % (
            self.__class__.__name__, ', '.join(options), self.timezone)
