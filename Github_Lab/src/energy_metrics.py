"""
energy_metrics.py
Practical analytics utilities for power systems.
"""

from math import sqrt


def compute_efficiency(input_power: float, output_power: float) -> float:
    """Efficiency (%) = (P_out / P_in) * 100"""
    if input_power <= 0:
        raise ValueError("input_power must be > 0")
    if output_power < 0:
        raise ValueError("output_power must be >= 0")
    return (output_power / input_power) * 100


def compute_power_factor(real_power: float, apparent_power: float) -> float:
    """Power factor = P / S"""
    if apparent_power <= 0:
        raise ValueError("apparent_power must be > 0")
    if real_power < 0:
        raise ValueError("real_power must be >= 0")
    pf = real_power / apparent_power
    return max(0.0, min(1.0, round(pf, 4)))


def rms(values: list[float]) -> float:
    """Root-mean-square of a list of values."""
    if not values:
        raise ValueError("values must be non-empty")
    return sqrt(sum(v * v for v in values) / len(values))


def thd_fundamental(v_fund: float, harmonics: list[float]) -> float:
    """Total Harmonic Distortion (THD, %)"""
    if v_fund <= 0:
        raise ValueError("v_fund must be > 0")
    if any(h < 0 for h in harmonics):
        raise ValueError("harmonics must be >= 0")
    num = sqrt(sum(h * h for h in harmonics))
    return (num / v_fund) * 100
