import random
def simulate_crashes(days):
    crashes = 0
    for i in range(days):
# Each day has a 4.5% chance of crashing
        if random.random() < 0.045:
            crashes += 1
    return crashes / days  

# Run the simulation for different sample sizes
for d in [30, 1000, 10000]:
    prob = simulate_crashes(d)
    print(f"Days: {d}, Simulated Crash Probability: {prob:.4f}")
'''Interpretation
 Law of Large Numbers (LLN)
The LLN states that as the number of trials increases, the average of the simulated outcomes converges to the true theoretical probability. In this case, the true crash probability is 0.045.
Small samples (like 30 days) can show misleadingly high or low crash rates.
Larger samples (like 10,000 days) smooth out randomness and align with the true probability.

If the startup bases its yearly maintenance budget on a small dataset, it risks serious miscalculations.
Example: If 8 crashes occur in 100 days, that's an 8% crash rate — almost double the true rate.
 Conversely, if only 2 crashes occur, that's 2% — less than half the true rate.
 Either case could lead to overestimating or underestimating costs, which is financially risky.
'''