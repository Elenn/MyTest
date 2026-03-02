import unittest

class TestPackageSorting(unittest.TestCase):
    def test_standard_package(self):
        # Not bulky, not heavy
        self.assertEqual(sort(100, 50, 20, 10), "STANDARD")

    def test_special_bulky_by_volume(self):
        # Volume >= 1,000,000
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")   # volume = 1,000,000

    def test_special_bulky_by_dimension(self):
        # One dimension >= 150
        self.assertEqual(sort(200, 50, 20, 10), "SPECIAL")
        self.assertEqual(sort(50, 150, 20, 10), "SPECIAL")
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")

    def test_special_heavy_only(self):
        # Heavy, not bulky
        self.assertEqual(sort(100, 50, 20, 20), "SPECIAL")
        self.assertEqual(sort(100, 50, 20, 25), "SPECIAL")

    def test_rejected_both_bulky_and_heavy(self):
        # Bulky by volume + heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        # Bulky by dimension + heavy
        self.assertEqual(sort(150, 50, 20, 20), "REJECTED")
        self.assertEqual(sort(100, 200, 30, 25), "REJECTED")

    def test_edge_cases(self):
        # Volume exactly 1,000,000 and mass exactly 20 → REJECTED
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        # Dimension exactly 150 and mass <20 → SPECIAL
        self.assertEqual(sort(150, 50, 30, 19), "SPECIAL")
        # Volume exactly 1,000,000 and mass <20 → SPECIAL
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")
        # Mass exactly 20 and not bulky → SPECIAL
        self.assertEqual(sort(100, 50, 30, 20), "SPECIAL")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort(0, 10, 10, 5)
        with self.assertRaises(ValueError):
            sort(10, -5, 10, 5)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, "20")  # non-numeric

if __name__ == "__main__":
    unittest.main()	