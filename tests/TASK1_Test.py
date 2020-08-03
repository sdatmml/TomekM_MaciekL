import unittest
from TomekM_MaciekL.geometry.TAKS1 import Geometry


class TestingGeometry(unittest.TestCase):

    def test01(self):
        self.assertEqual(Geometry.section_center((1, 1, 1), (3, 3, 3)), (2, 2, 2))

    def test02(self):
        self.assertEqual(Geometry.section_center((1, 1, 1), (2, 2, 2)), (1.5, 1.5, 1.5))

    def test03(self):
        with self.assertRaises(Exception) as context:
            Geometry.section_center((1, 1, 1), (1, 1, 1))
            self.assertTrue('Data is no section error', context.exception)
