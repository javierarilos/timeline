import unittest
import timeline
from datetime import datetime

a_format = '%Y-%m-%d %H:%M:%S'
a_timeline = [
    ['2015-10-22 13:15:20', 'donald', 'mickey', 'supper together', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:21', 'mickey', 'pluto', 'party', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:22', 'daisy', 'minnie', 'brunch?', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:22', 'donald', 'daisy', 'drinks?', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:22', 'pluto', 'goofy', 'going to the movies', 'hi there, how about tonight'],
    ['2015-10-22 13:15:23', 'donald', 'minnie', 'important update', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:23', 'donald', 'goofy', 'football on sunday', 'hi there, how about tonight'],
    ['2015-10-22 13:15:24', 'goofy', 'micky', 'TIMELINErestriction', 'ts must be sorted, old 2 new']
]


def test_cb(original_datetime, *args):
    print('called back from', original_datetime)


class TestTimeline(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_timeline_creation(self):
        timln = timeline.Timeline(test_cb, ts_col=1, ts_fmt=a_format)

        self.assertEqual(timln.ts_col, 1)
        self.assertEqual(timln.ts_fmt, a_format)
        self.assertEqual(timln.callback, test_cb)

    def test_timeline_callback_mandatory(self):
        with self.assertRaises(Exception):
            timln = timeline.Timeline(None)

    def test_is_valid_ko_non_iterable(self):
        timln = timeline.Timeline(test_cb, ts_col=0, ts_fmt=a_format)

        is_valid = timln.is_valid(234)

        self.assertFalse(is_valid)

    def test_is_valid_ko_short_timeline(self):
        timln = timeline.Timeline(test_cb, ts_col=0, ts_fmt=a_format)

        empty_timeline = timln.parse([])
        self.assertFalse(timln.is_valid(empty_timeline))

        tooshort_timeline = timln.parse([
            ['2015-10-22 13:15:20', 'donald', 'mickey']
        ])
        self.assertFalse(timln.is_valid(tooshort_timeline))

    def test_is_valid_ko_unsorted_timedates(self):
        timln = timeline.Timeline(test_cb, ts_col=0, ts_fmt=a_format)

        unsorted_timeline = timln.parse([
            ['2015-10-22 13:15:21', 'mickey', 'pluto', 'yay'],
            ['2015-10-22 13:15:20', 'donald', 'mickey']
        ])  # second event ts is before firt's

        is_valid = timln.is_valid(unsorted_timeline)

        self.assertFalse(is_valid)

    def test_is_valid_ok(self):
        timln = timeline.Timeline(test_cb, ts_col=0, ts_fmt=a_format)

        is_valid = timln.is_valid(a_timeline)

        self.assertTrue(is_valid)

    def test_parse_ok(self):
        timln = timeline.Timeline(test_cb, ts_col=0, ts_fmt=a_format)

        test_timeline = [
            ['2015-10-22 13:15:20', 'donald', 'mickey'],
            ['2015-10-22 13:15:21', 'mickey', 'pluto', 'yay']
        ]

        parsed_timeline = timln.parse(test_timeline)

        for parsed_row, original_row in zip(parsed_timeline, test_timeline):
            parsed_datetime = parsed_row[0]
            self.assertIsInstance(parsed_datetime, datetime)
            self.assertEqual(parsed_datetime.year, 2015)
            self.assertEqual(parsed_datetime.month, 10)
            self.assertEqual(parsed_datetime.day, 22)
            self.assertEqual(parsed_datetime.hour, 13)
            self.assertEqual(parsed_datetime.minute, 15)

            self.assertEqual(len(parsed_row), len(original_row)+1)
            self.assertEqual(parsed_row[1:], original_row)

    def test_parse_ko_bad_dateformat(self):
        timln = timeline.Timeline(test_cb, ts_col=0, ts_fmt=a_format)

        test_timeline = [
            ['BADDATEFORMAT', 'donald', 'mickey'],
            ['2015-10-22 13:15:21', 'mickey', 'pluto', 'yay']
        ]

        with self.assertRaises(ValueError):
            parsed_timeline = timln.parse(test_timeline)
