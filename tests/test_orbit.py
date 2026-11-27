import math
import unittest
from research.orbit import circular_orbit

class CircularOrbitTests(unittest.TestCase):
    def test_low_earth_orbit(self):
        speed, period = circular_orbit(400)
        self.assertAlmostEqual(speed, 7.67, places=2)
        self.assertTrue(92 < period < 94)

    def test_higher_orbit(self):
        speed, period = circular_orbit(35786)
        self.assertTrue(3.07 < speed < 3.08)
        self.assertTrue(1435 < period < 1437)

    def test_invalid(self):
        for value in (0, -1, math.nan, math.inf):
            with self.subTest(value=value), self.assertRaises(ValueError):
                circular_orbit(value)

    def test_monotonic(self):
        v1, t1 = circular_orbit(400)
        v2, t2 = circular_orbit(800)
        self.assertLess(v2, v1)
        self.assertGreater(t2, t1)
