#!/usr/bin/env python
"""Calculates caloric consumption based on data gather from
    Under Armour caloric estimates.
"""

__author__ = "Alice Seaborn"

__version__ = "0.0.0"
__maintainer__ = "Alice Seaborn"
__email__ = "seaborn.dev@gmail.com"
__status__ = "Prototype"



def _calc_pounds_to_kg(pounds):
    return pounds/2.205


def under_armour_cycling_met_units(speed):
    return (0.971*speed) - 3.84


def under_armour_calories_per_minute(weight, speed):
    mets = under_armour_cycling_met_units(speed)
    weight = _calc_pounds_to_kg(weight)
    return 0.0175*mets*weight


def under_armour_calc_total_calories_burned(weight, duration, speed):
    calories_per_minute = under_armour_calories_per_minute(weight, speed)
    return calories_per_minute*duration



if __name__ == '__main__':
    print("The Under Armor cycling model cannot be run as an executable.")
