#!/usr/bin/env python
"""Calculates caloric consumption based on the discrete MET model.
"""

__author__ = "Alice Seaborn"

__version__ = "0.0.0"
__maintainer__ = "Alice Seaborn"
__email__ = "seaborn.dev@gmail.com"
__status__ = "Prototype"


def _calc_pounds_to_kg(pounds):
    return pounds/2.205


def dmet_cycling_met_units(speed):
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


def dmet_calories_per_minute(weight, speed):
    mets = dmet_cycling_met_units(speed)
    weight = _calc_pounds_to_kg(weight)
    return 0.0175*mets*weight


def dmet_calc_total_calories_burned(weight, duration, speed):
    calories_per_minute = dmet_calories_per_minute(weight, speed)
    return calories_per_minute*duration


if __name__ == '__main__':
    print("The discrete cycling model cannot be run as an executable.")
