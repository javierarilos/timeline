#!/usr/bin/env python
""" Timeline
"""
import sys


class Timeline:
    def __init__(self, callback, ts_col=1, ts_fmt='%Y-%m-%d %H:%M:%S'):
        if not callback:
            raise Exception('callback is mandatory')
        self.callback = callback
        self.ts_col = ts_col
        self.ts_fmt = ts_fmt
