"""This module contains several handy functions primarily meant for internal use."""

from __future__ import division

from calendar import timegm
from datetime import date, datetime, time, timedelta, tzinfo


def asint(text):
    """
    Safely converts a string to an integer, returning ``None`` if the string is ``None``.

    :type text: str
    :rtype: int

    """
    if text is not None:
        return int(text)


def datetime_ceil(dateval):
    """
    Rounds the given datetime object upwards.

    :type dateval: datetime

    """
    if dateval.microsecond > 0:
        return dateval + timedelta(seconds=1, microseconds=-dateval.microsecond)
    return dateval


def datetime_repr(dateval):
    return dateval.strftime('%Y-%m-%d %H:%M:%S %Z') if dateval else 'None'


def normalize(dt):
    return datetime.fromtimestamp(dt.timestamp(), dt.tzinfo)


def localize(dt, tzinfo):
    if hasattr(tzinfo, 'localize'):
        return tzinfo.localize(dt)

    return normalize(dt.replace(tzinfo=tzinfo))
