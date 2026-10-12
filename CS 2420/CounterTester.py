import unittest
from Counter import Counter

class TestCounter(unittest.TestCase):
    def test_initial_count(self):
        counter = Counter()
        self.assertEqual(counter.get_count(), 0)

    def test_increment(self):
        counter = Counter()
        counter.incrementCount()
        self.assertEqual(counter.get_count(), 1)
        counter.incrementCount()
        self.assertEqual(counter.get_count(), 2)

    def test_reset(self):
        counter = Counter()
        counter.incrementCount()
        self.assertGreater(counter.get_count(), 0)
        counter.resetCount()
        self.assertEqual(counter.get_count(), 0)

if __name__ == "__main__":
    unittest.main()