import unittest
from TomekM_MaciekL.statistics_.TASK2 import SimpleSequenceCalc
from math import sqrt


class TestCalc(unittest.TestCase):

    def test1(self):
        self.assertEqual(SimpleSequenceCalc.sqrt_from_avg_of_sequence([1, 1, 1]), sqrt(3))

    def test2(self):
        with self.assertRaises(Exception) as context:
            SimpleSequenceCalc.sqrt_from_avg_of_sequence([1, 1, -1])
            self.assertTrue('ValueError', context.exception)

    def test3(self):
        with self.assertRaises(Exception) as context:
            SimpleSequenceCalc.sqrt_from_avg_of_sequence([1, 1, 0])
            self.assertTrue('ZeroDivisionError', context.exception)

    def test4(self):
        with self.assertRaises(Exception) as context:
            SimpleSequenceCalc.sqrt_from_avg_of_sequence([-1, -1, -1])
            self.assertTrue('ValueError', context.exception)

    def test5(self):
        self.assertEqual(SimpleSequenceCalc.sqrt_from_avg_of_sequence([-7, 1,]), sqrt(-6/-7))