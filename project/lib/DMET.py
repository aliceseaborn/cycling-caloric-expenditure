#!/usr/bin/env python
"""Calculates caloric consumption based on the discrete MET model.
"""

__author__ = "Alice Seaborn"

__version__ = "0.0.0"
__maintainer__ = "Alice Seaborn"
__email__ = "seaborn.dev@gmail.com"
__status__ = "Prototype"


class DMET(object):
    
    def __init__(self):
        """
        Input: None.
        Output: DMET instance.
        """

    def _lbs_to_kg(self, pounds):
        return pounds/2.205

    def met_units(self, speed):
        """
        Input: Average speed in mph.
        Output: Estimated MET units.
        """
        if speed <= 10.0:
            return 4
        elif speed <= 11.99:
            return 6
        elif speed <= 13.99:
            return 8
        elif speed <= 15.99:
            return 10
        elif speed <= 19.99:
            return 12
        else:
            return 14

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
    print("The discrete cycling model cannot be run as an executable.")
