import unittest
from cbc import activity_converter


class ActivityTest(unittest.TestCase):
    def test_sedentary(self):
        self.assertEqual('sedentary', activity_converter('1'))

    def test_light(self):
        self.assertEqual('light', activity_converter('2'))

    def test_moderate(self):
        self.assertEqual('moderate', activity_converter('3'))

    def test_active(self):
        self.assertEqual('active', activity_converter('4'))

    def test_zero(self):
        self.assertEqual('Invalid input', activity_converter('0'))

    def test_five(self):
        self.assertEqual('Invalid input', activity_converter('5'))

    def test_int(self):
        self.assertEqual('Invalid input', activity_converter(3))

    def test_word(self):
        self.assertEqual('Invalid input', activity_converter('three'))


if __name__ == '__main__':
    unittest.main()
