This project implements a pure-Python statistical engine and a Monte Carlo simulation to demonstrate key statistical concepts such as central tendency, dispersion, outlier detection, and the Law of Large Numbers (LLN).
The goal is to analyze raw data (e.g., startup salaries) and simulate probabilistic scenarios (e.g., server crashes) without relying on external libraries beyond Python’s standard library.
## Mathematical Logic
                 Central Tendency

1. Mean: Arithmetic average of all values.
2. Median: Middle value when data is sorted.
.If odd length → middle element.
 If even length → average of the two middle elements.
3. Mode: Most frequently occurring value(s).
 Handles multimodal distributions by returning all modes.
 Returns a message if all values are unique.
               Dispersion
Variance: is a fundamental concept in statistics that measures how spread out a set of numbers is
Population Variance (when you have data for the entire population):
   Population Variance: \sigma ^2=\frac{\sum (x_i-\mu )^2}{N}
    --> where  n = number of data points in the sample
Sample Variance (when you have a sample from a population):
      Sample Variance (Bessel’s correction): s^2=\frac{\sum (x_i-\bar {x})^2}{N-1}
   -->  where n-1 is called Bessel’s correction, which corrects for bias when estimating population variance from a sample.

--> Standard Deviation: Square root of variance.
Outlier Detection
 A data point is considered an outlier if it lies more than threshold standard deviations from the mean.
       -Default threshold = 2.

 Monte Carlo Simulation (Law of Large Numbers)
         Scenario
 A server has a 4.5% chance of crashing on any given day.
 Function simulate_crashes(days) simulates crashes over a given number of days.
              Results
 30 days → Probability fluctuates significantly.
 1,000 days → Probability stabilizes closer to 0.045.
 10,000 days → Probability converges very close to 0.045.
           Interpretation
The Law of Large Numbers states that as the number of trials increases, the simulated probability converges to the theoretical probability.
>> For startups, relying on small datasets (like 30 days) is dangerous because short-term volatility can mislead budget planning.
## Setup Instructions

. Clone the repository:
git clone https://github.com/yourusername/statistical_engine.git
cd statistical_engine
Ensure Python 3.x is installed. No external packages are required.
Run the main program:
This project uses Python’s built-in unittest framework.

Run all tests:
>python -m unittest discover -s tests
Tests cover:
Mean and median calculations (odd & even lists)
Mode calculation (including multimodal and unique datasets)
Sample vs population variance
Standard deviation
Handling of empty lists and invalid data

## Acceptance Criteria Checklist
 Passes empty list handling – The engine does not crash and returns a descriptive message when given an empty dataset.
 Handles non-numeric or mixed data – Cleans or rejects invalid entries such as strings, None, or dictionaries.
 Correctly calculates mean – Works for odd, even, and mixed datasets.
 Correctly calculates median – Handles both odd and even-length datasets accurately.
 Correctly calculates mode – Returns all modes for multimodal datasets and a message if all values are unique.
 Accurately calculates sample variance – Uses Bessel’s correction (n-1) for unbiased estimation.
 Accurately calculates population variance – Divides by n for full dataset variance.
 Correct standard deviation calculation – Matches the square root of the correct variance.
 Detects outliers – Returns values beyond a configurable number of standard deviations from the mean.
 Monte Carlo simulation works – Simulated probabilities converge toward theoretical probability as the number of trials increases, demonstrating the Law of Large Numbers.
 Fully documented, professional folder structure – All files are organized in src/, tests/, data/, and the project includes README and main.py.
 All unit tests pass successfully – Tests cover all above features and edge cases using Python’s unittest.