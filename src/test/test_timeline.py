import unittest
import timeline

a_format = '%Y-%m-%d %H:%M:%S'

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
