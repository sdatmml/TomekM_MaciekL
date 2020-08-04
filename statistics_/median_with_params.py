import statistics
from typing import List
from math import pi, e


class MathFunc:

    @staticmethod
    def calculate_median_with_params(num_set: List[int]) -> float:
        return round(statistics.median(num_set)*0.5*pi+e, 2)

