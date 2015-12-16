import unittest
import event_list
from datetime import datetime


class TestEventListFromCsv(unittest.TestCase):
    def test_from_csv(self):
        el = event_list.from_csv('test/sample_timeline.csv')

        self.assertEqual(len(el), 8)
        self.assertEqual(el[0][1], 'donald')
        self.assertEqual(el[0][2], 'mickey')
        self.assertEqual(el[7][1], 'goofy')
        self.assertEqual(el[7][2], 'mickey')
