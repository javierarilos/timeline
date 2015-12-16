#!/usr/bin/env python
""" Timeline
"""
import sys
from datetime import datetime


class Timeline:
    def __init__(self, callback, ts_col=0, ts_fmt='%Y-%m-%d %H:%M:%S'):
        if not callback:
            raise Exception('callback is mandatory')
        self.callback = callback
        self.ts_col = ts_col
        self.ts_fmt = ts_fmt
        self.events = []

    def parse(self, event_list):
        """Parses event_list[:][ts_col] to datetime using ts_fmt

        Returns a new list of rows (lists) where
            row first column is the parsed datetime, the rest is the original row
        """
        return list(map(lambda event: [datetime.strptime(event[0], self.ts_fmt)] + event, event_list))

    def is_valid(self, event_list, skip_first=False):
        """Validates event_list, returns True on valid list.
        - event_list is expected to: be a parsed event_list (see self.parse)
            events in event_list must be sorted by date from old to new.
        - skip_first indicates if first row should be skipped (eg: contains headers)
        """
        if not isinstance(event_list, list):
            return False
        if len(event_list) < 2:
            return False

        first_row = 1 if skip_first else 0
        previous_ts = event_list[first_row][self.ts_col]
        for row in event_list[first_row+1:]:
            curr_ts = row[self.ts_col]
            if curr_ts < previous_ts:
                return False
        return True

    def start(self, event_list, skip_first=False):
        """Starts calling back self.callback following the timeline specified by event_list.
        event_list is expected to be valid
        """
        parsed_event_list = self.parse(event_list)
        is_valid = self.is_valid(parsed_event_list, skip_first=skip_first)
        if not is_valid:
            import json
            raise Exception('Given event list is not valid.' + json.dumps(parsed_event_list,
                            sort_keys=False, indent=4, separators=(',', ': ')))
