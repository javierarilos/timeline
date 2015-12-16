from datetime import datetime
from time import sleep

def from_parse_datetimes(ts_fmt, ts_col, event_list):
    """
    Returns a planning list by parsing datetimes in event_list[:][ts_col] to datetime using ts_fmt

    Returns a new list of rows (lists) where
        first column is the parsed datetime, the rest is the original row
    """
    return [[datetime.strptime(evt[ts_col], ts_fmt)] + evt for evt in event_list]

def is_valid(planning):
    """Validates planning, returns True on valid list.
    - planning is expected to: be a parsed planning (see self.parse)
        events in planning must be sorted by date from old to new.
    """
    if not isinstance(planning, list):
        return False

    if len(planning) < 2:
        return False

    # datetimes must be sorted by date from old to new.
    previous_ts = planning[0][0]
    for row in planning[1:]:
        curr_ts = row[0]
        if curr_ts < previous_ts:
            return False

    return True

def start(planning, callback):
    """Starts calling back self.callback following the timeline specified by event_list.
    event_list is expected to be valid
    """
    previous_ts = planning[0][0]
    for row in planning:
        curr_ts = row[0]
        increment = (curr_ts - previous_ts).seconds
        sleep(increment)
        callback(*row[1:])
        previous_ts = curr_ts
