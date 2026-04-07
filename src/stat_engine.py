import math
from typing import List, Union
class StatEngine:
    def __init__(self, data: Union[List, tuple]):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Data must be provided as a list or tuple.")

        # Clean data: keep only numeric values, skip None/empty strings
        cleaned = []
        for item in data:
            if isinstance(item, (int, float)):
                cleaned.append(item)
            elif item is None or item == "":
                continue
            else:
                raise TypeError(
                    f"Invalid data type detected: {item} ({type(item).__name__})"
                )

        if len(cleaned) == 0:
            raise ValueError("Data list is empty or contains no valid numeric values.")

        self.data = cleaned

    # 1.Central Tendency 
    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self):
        freq = {}
        for val in self.data:
            freq[val] = freq.get(val, 0) + 1

        max_count = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_count]

        if len(modes) == len(freq):  # all values unique
            return "All values are unique, no mode"
        elif len(modes) == 1:
            return modes[0]
        else:
            return modes  # multimodal case

    # 2.Dispersion
    def get_variance(self, is_sample=True):
        n = len(self.data)
        if n < 2 and is_sample:
            return "Sample variance requires at least two data points"

        mean = self.get_mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]

        if is_sample:
            return sum(squared_diffs) / (n - 1)  # Bessel’s correction
        else:
            return sum(squared_diffs) / n  # population variance

    def get_standard_deviation(self, is_sample=True):
        var = self.get_variance(is_sample=is_sample)
        if isinstance(var, str):  # error message case
            return var
        return math.sqrt(var)

    #3. Outlier Detection
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        stdev = self.get_standard_deviation()
        if isinstance(stdev, str): 
            return []
        return [x for x in self.data if abs(x - mean) > threshold * stdev]

data = [1, 2, '3', None, 5, 5, 10]

try:
    engine = StatEngine(data)
    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Variance (sample):", engine.get_variance(is_sample=True))
    print("Variance (population):", engine.get_variance(is_sample=False))
    print("Standard Deviation:", engine.get_standard_deviation())
    print("Outliers:", engine.get_outliers(threshold=2))
except (TypeError, ValueError) as e:
    print("Error:", e)
