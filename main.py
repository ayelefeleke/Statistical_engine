
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes
import json
def main():
    # 1. Load mock salary data
    try:
        with open("data/sample_salaries.json") as f:
            salaries = json.load(f)
    except FileNotFoundError:
        print("Salary data file not found. Please create 'sample_salaries.json' in /data/")
        return
    # 2. Create StatEngine instance
    try:
        engine = StatEngine(salaries)
    except (ValueError, TypeError) as e:
        print("Error initializing StatEngine:", e)
        return
    # 3. Compute statistics
    
    print("Salary Statistics")
    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Variance (sample):", engine.get_variance(is_sample=True))
    print("Standard Deviation (sample):", engine.get_standard_deviation(is_sample=True))
    print("Outliers (2 std dev):", engine.get_outliers())

    # 4. Monte Carlo Simulation
    print("\n=Server Crash Simulation:")
    for days in [30, 1000, 10000]:
        prob = simulate_crashes(days)
        print(f"Simulated probability over {days} days: {prob:.4f}")

    # 5. Interpretation
    print("\nInterpretation:")
    print("The 30-day simulation may vary significantly from the theoretical probability (0.045).")
    print("As the number of days increases, simulated probability approaches 0.045, demonstrating the Law of Large Numbers.")
    print("This shows why small sample data can be misleading for predictions.")

if __name__ == "__main__":
    main()