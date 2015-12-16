#!/usr/bin/env python
""" Timeline
"""
import sys
from datetime import datetime
import planning


class Timeline:
    def __init__(self, callback, ts_col=0, ts_fmt='%Y-%m-%d %H:%M:%S'):
        if not callback:
            raise Exception('callback is mandatory')
        self.callback = callback
        self.ts_col = ts_col
        self.ts_fmt = ts_fmt
        self.events = []

    def parse(self, event_list):
        return planning.from_parse_datetimes(self.ts_fmt, self.ts_col, event_list)

    def is_valid(self, planning_lst):
        return planning.is_valid(planning_lst)

    def start(self, event_list, skip_first=False):
        """Starts calling back self.callback following the timeline specified by event_list.
        event_list is expected to be valid
        """
        planning = self.parse(event_list)
        is_valid = planning.is_valid(planning, skip_first=skip_first)
        if not is_valid:
            import json
            raise Exception('Given planning is not valid.' + json.dumps(planning,
                            sort_keys=False, indent=4, separators=(',', ': ')))

        first_row = 1 if skip_first else 0
        previous_ts = event_list[first_row][self.ts_col]
        for row in event_list[first_row:]:
            curr_ts = row[self.ts_col]
            sleep((curr_ts - previous_ts).seconds)
            self.callback(*row[1:])
            previous_ts = curr_ts
