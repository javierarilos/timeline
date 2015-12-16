from datetime import datetime
def from_parse_datetimes(ts_fmt, ts_col, event_list):
    """
    Returns a planning list by parsing datetimes in event_list[:][ts_col] to datetime using ts_fmt

    Returns a new list of rows (lists) where
        first column is the parsed datetime, the rest is the original row
    """
    return [[datetime.strptime(evt[ts_col], ts_fmt)] + evt for evt in event_list]
