#!/usr/bin/env python
"""Uses the continuous MET model to calculate caloric consumption.
"""

import numpy as np

__author__ = "Alice Seaborn"

__version__ = "0.0.0"
__maintainer__ = "Alice Seaborn"
__email__ = "seaborn.dev@gmail.com"
__status__ = "Prototype"


class CMET(object):
    
    def __init__(self):
        """
        Input: None.
        Output: CMET instance.
        """
        self.coefficients = np.array([3.19343066e-03, -6.25952515e-02,
                                      5.62785754e-01, 3.98022780e+00])

    def _lbs_to_kg(self, pounds):
        return pounds/2.205
    
    def met_units(self, speed):
        """
        Input: Average speed in mph.
        Output: Estimated MET units.
        """
        polynomial = np.poly1d(self.coefficients)
        return polynomial(speed)
    
    def calories_per_minute(self, speed, weight):
        """
        Input: Average speed in mph. Weight in pounds.
        Output: Estimated calories burned per minute.
        """
        mets = self.met_units(speed)
        weight = self._lbs_to_kg(weight)
        return 0.0175*mets*weight
    
    def total_calories(self, speed, weight, duration):
        """
        Input: Average speed in mph.  Weight in pounds.
            Duration of ride in minutes.
        Output: Total estimated calories burned.
        """
        cpm = self.calories_per_minute(speed, weight)
        return cpm*duration


if __name__ == '__main__':
    print("The continuous cycling model cannot be run as an executable.")
