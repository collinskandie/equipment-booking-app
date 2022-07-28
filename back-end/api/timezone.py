import datetime
import sqlite3

def tz_aware_timestamp_adapter(val):
    datepart, timepart = val.split(b" ")
    year, month, day = map(int, datepart.split(b"-"))

    if b"+" in timepart:
        timepart, tz_offset = timepart.rsplit(b"+", 1)
        if tz_offset == b'00:00':
            tzinfo = datetime.timezone.utc
        else:
            hours, minutes = map(int, tz_offset.split(b':', 1))
            tzinfo = datetime.timezone(datetime.timedelta(hours=hours, minutes=minutes))
    else:
        tzinfo = None

    timepart_full = timepart.split(b".")
    hours, minutes, seconds = map(int, timepart_full[0].split(b":"))

    if len(timepart_full) == 2:
        microseconds = int('{:0<6.6}'.format(timepart_full[1].decode()))
    else:
        microseconds = 0

    val = datetime.datetime(year, month, day, hours, minutes, seconds, microseconds, tzinfo)

    return val

sqlite3.register_converter('timestamp', tz_aware_timestamp_adapter)