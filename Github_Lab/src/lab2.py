"""
lab.py
Main script to demonstrate and validate the energy metrics module.
"""

from energy_metrics import (
    compute_efficiency,
    compute_power_factor,
    rms,
    thd_fundamental,
)

def main():
    print("🔋 Energy Metrics Demonstration\n" + "-" * 40)

    # Efficiency example
    input_power = 100.0
    output_power = 85.0
    eff = compute_efficiency(input_power, output_power)
    print(f"Efficiency: {eff:.2f}% (for {output_power}W out of {input_power}W)")

    # Power factor example
    real_power = 900.0
    apparent_power = 1000.0
    pf = compute_power_factor(real_power, apparent_power)
    print(f"Power Factor: {pf}")

    # RMS example
    values = [0.0, 3.0, 4.0]
    result_rms = rms(values)
    print(f"RMS of {values} = {result_rms:.4f}")

    # THD example
    v_fundamental = 230.0
    harmonics = [5.0, 3.0]
    thd = thd_fundamental(v_fundamental, harmonics)
    print(f"THD: {thd:.2f}% for harmonics {harmonics} on {v_fundamental} Vrms")

    print("\n✅ All computations done successfully!")

if __name__ == "__main__":
    main()
