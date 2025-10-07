import math
import pytest
from src import energy_metrics as em


def test_compute_efficiency():
    assert em.compute_efficiency(100, 85) == 85.0
    assert em.compute_efficiency(200, 150) == 75.0
    with pytest.raises(ValueError):
        em.compute_efficiency(0, 10)
    with pytest.raises(ValueError):
        em.compute_efficiency(-10, 5)
    with pytest.raises(ValueError):
        em.compute_efficiency(100, -5)


def test_compute_power_factor():
    assert em.compute_power_factor(900, 1000) == 0.9
    assert em.compute_power_factor(1, 3) == 0.3333
    assert em.compute_power_factor(1200, 1000) == 1.0
    with pytest.raises(ValueError):
        em.compute_power_factor(-1, 100)
    with pytest.raises(ValueError):
        em.compute_power_factor(10, 0)


def test_rms():
    # sqrt((0^2+3^2+4^2)/3) = sqrt(25/3) ≈ 2.88675
    assert round(em.rms([0, 3, 4]), 5) == 2.88675
    with pytest.raises(ValueError):
        em.rms([])


def test_thd_fundamental():
    thd = em.thd_fundamental(230, [5, 3])
    # sqrt(25+9)/230*100 ≈ 2.5352 → 2.54 after rounding
    assert round(thd, 2) == 2.54
    assert em.thd_fundamental(230, []) == 0.0
    with pytest.raises(ValueError):
        em.thd_fundamental(0, [1])
    with pytest.raises(ValueError):
        em.thd_fundamental(230, [1, -1])
