import math
import unittest
from src import energy_metrics as em


class TestEnergyMetrics(unittest.TestCase):
    def test_efficiency(self):
        self.assertEqual(em.compute_efficiency(100, 85), 85.0)
        self.assertEqual(em.compute_efficiency(200, 150), 75.0)
        with self.assertRaises(ValueError):
            em.compute_efficiency(0, 10)

    def test_power_factor(self):
        self.assertEqual(em.compute_power_factor(900, 1000), 0.9)
        self.assertEqual(em.compute_power_factor(1, 3), 0.3333)
        self.assertEqual(em.compute_power_factor(1200, 1000), 1.0)
        with self.assertRaises(ValueError):
            em.compute_power_factor(-5, 100)

    def test_rms(self):
        val = em.rms([0, 3, 4])
        # expected = sqrt(25/3) ≈ 2.886751...
        self.assertTrue(math.isclose(val, 2.8867513459, rel_tol=1e-9, abs_tol=1e-12))
        with self.assertRaises(ValueError):
            em.rms([])

    def test_thd(self):
        thd = em.thd_fundamental(230, [5, 3])
        # expected ≈ 2.535196...%
        self.assertTrue(math.isclose(thd, 2.535196, rel_tol=1e-6))
        self.assertEqual(em.thd_fundamental(230, []), 0.0)
        with self.assertRaises(ValueError):
            em.thd_fundamental(0, [5])


if __name__ == "__main__":
    unittest.main()
