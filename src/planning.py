from datetime import datetime
def parse(ts_fmt, ts_col, event_list):
    """
    Parses datetimes in event_list[:][ts_col] to datetime using ts_fmt

    Returns a new list of rows (lists) where
        first column is the parsed datetime, the rest is the original row
    """
    return [[datetime.strptime(evt[ts_col], ts_fmt)] + evt for evt in event_list]
