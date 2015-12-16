import unittest
import planning
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


def test_cb(*args):
    print('-> called back from', args)


class TestPlanningIsValid(unittest.TestCase):
    def test_is_valid_ko_non_iterable(self):
        is_valid = planning.is_valid(234)

        self.assertFalse(is_valid)

    def test_is_valid_ko_short_timeline(self):
        empty_timeline = planning.from_parse_datetimes(a_format, 0, [])
        is_empty_valid = planning.is_valid(empty_timeline)
        self.assertFalse(is_empty_valid)

        only_one_event = [['2015-10-22 13:15:20', 'donald', 'mickey']]
        tooshort_timeline = planning.from_parse_datetimes(a_format, 0, only_one_event)
        is_too_short_valid = planning.is_valid(tooshort_timeline)
        self.assertFalse(is_too_short_valid)

    def test_is_valid_ko_unsorted_timedates(self):
        unsorted_planning = planning.from_parse_datetimes(a_format, 0, [
            ['2015-10-22 13:15:21', 'mickey', 'pluto', 'yay'],
            ['2015-10-22 13:15:20', 'donald', 'mickey']
        ])  # second event ts is before firt's

        is_unsorted_valid = planning.is_valid(unsorted_planning)

        self.assertFalse(is_unsorted_valid)

    def test_is_valid_ok(self):
        ok_planning = planning.from_parse_datetimes(a_format, 0, a_timeline)

        is_valid_ok_planning = planning.is_valid(ok_planning)

        self.assertTrue(is_valid_ok_planning)


class TestPlanningFromParseDatetimes(unittest.TestCase):
    def test_parse_ok(self):
        test_timeline = [
            ['2015-10-22 13:15:20', 'donald', 'mickey'],
            ['2015-10-22 13:15:21', 'mickey', 'pluto', 'yay']
        ]

        parsed_planning = planning.from_parse_datetimes(a_format, 0, test_timeline)

        for parsed_row, original_row in zip(parsed_planning, test_timeline):
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
        test_timeline = [
            ['BADDATEFORMAT', 'donald', 'mickey'],
            ['2015-10-22 13:15:21', 'mickey', 'pluto', 'yay']
        ]

        with self.assertRaises(ValueError):
            parsed_planning = planning.from_parse_datetimes(a_format, 0, test_timeline)
