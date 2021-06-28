#!/usr/bin/env python
"""Calculates caloric consumption based on data gather from
    Under Armour caloric estimates.
"""

__author__ = "Alice Seaborn"

__version__ = "0.0.0"
__maintainer__ = "Alice Seaborn"
__email__ = "seaborn.dev@gmail.com"
__status__ = "Prototype"


class UnderArmour(object):
    
    def __init__(self):
        """
        Input: None.
        Output: Under Armour estimator instance.
        """

    def _lbs_to_kg(self, pounds):
        return pounds/2.205

    def met_units(self, speed):
        """
        Input: Average speed in mph.
        Output: Estimated MET units.
        """
        return (0.971*speed) - 3.84
    
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
    print("The Under Armor cycling model cannot be run as an executable.")
