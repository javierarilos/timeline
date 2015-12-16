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
        - event_list is expected to: contain lists or tuples with a parseable datetime
            in column self.ts_col using self.ts_fmt
            events in event_list must be sorted by date from old to new.
        - skip_first indicates if first row should be skipped (eg: contains headers)
        """
        if not isinstance(event_list, list):
            return False
        event_list_parsed = self.parse(event_list)
        return True

    def start(self, event_list, skip_first=False):
        """Starts calling back self.callback following the timeline specified by event_list.

        event_list is expected to be valid
        """
        parsed_event_list = self.parse(event_list)
        self.validate(event_list, skip_first=skip_first)
