from src.energy_metrics import (
    compute_efficiency,
    compute_power_factor,
    rms,
    thd_fundamental,
)


def main():
    print("🔋 Energy Metrics Demo")
    print("----------------------")
    print("Efficiency(100W→85W):", compute_efficiency(100, 85), "%")
    print("Power factor(900/1000):", compute_power_factor(900, 1000))
    print("RMS([0,3,4]):", rms([0, 3, 4]))
    print("THD(230V, [5,3]):", round(thd_fundamental(230, [5, 3]), 2), "%")


if __name__ == "__main__":
    main()
