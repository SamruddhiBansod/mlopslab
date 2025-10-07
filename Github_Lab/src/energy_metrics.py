"""
energy_metrics.py
Utility functions for basic power system metrics.
"""

from math import sqrt
from typing import List


def compute_efficiency(input_power: float, output_power: float) -> float:
    """
    Efficiency (%) = (P_out / P_in) * 100
    Raises:
        ValueError: if input_power <= 0 or output_power < 0
    """
    if input_power <= 0:
        raise ValueError("input_power must be > 0")
    if output_power < 0:
        raise ValueError("output_power must be >= 0")
    return (output_power / input_power) * 100.0


def compute_power_factor(real_power: float, apparent_power: float) -> float:
    """
    Power factor = P / S (rounded to 4 decimals, clipped to [0, 1])
    Raises:
        ValueError: if apparent_power <= 0 or real_power < 0
    """
    if apparent_power <= 0:
        raise ValueError("apparent_power must be > 0")
    if real_power < 0:
        raise ValueError("real_power must be >= 0")
    pf = real_power / apparent_power
    return max(0.0, min(1.0, round(pf, 4)))


def rms(values: List[float]) -> float:
    """
    Root-mean-square of a list of values.
    Raises:
        ValueError: if values is empty
    """
    if not values:
        raise ValueError("values must be non-empty")
    return sqrt(sum(v * v for v in values) / len(values))


def thd_fundamental(v_fund: float, harmonics: List[float]) -> float:
    """
    Total Harmonic Distortion (%) relative to the fundamental.
    THD = sqrt(sum(h^2)) / v_fund * 100
    Raises:
        ValueError: if v_fund <= 0 or any harmonic < 0
    """
    if v_fund <= 0:
        raise ValueError("v_fund must be > 0")
    if any(h < 0 for h in harmonics):
        raise ValueError("harmonics must be >= 0")
    if not harmonics:
        return 0.0
    return (sqrt(sum(h * h for h in harmonics)) / v_fund) * 100.0
