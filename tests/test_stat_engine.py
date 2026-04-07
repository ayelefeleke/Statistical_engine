import sys
import os

# Add project root to path so src can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.stat_engine import StatEngine
import unittest
from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    # Mean Test
    def test_mean(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_mean(), 2.5)

    # Median Odd
    def test_median_odd(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_median(), 2)

    # Median Even
    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    # Empty List Handling
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    # Known Standard Deviation Test
    def test_standard_deviation(self):
        engine = StatEngine([2,4,4,4,5,5,7,9])
        self.assertAlmostEqual(
            engine.get_standard_deviation(is_sample=False),
            2.0
        )


if __name__ == "__main__":
    unittest.main()