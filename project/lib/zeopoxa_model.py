#!/usr/bin/env python
"""Calculates caloric consumption based on data gather from
    Zeopoxa caloric estimates.
"""

__author__ = "Austin Dial, Alice Seaborn"

__version__ = "0.0.0"
__maintainer__ = "Alice Seaborn"
__email__ = "adial@mail.bradley.edu"
__status__ = "Prototype"



def _calc_pounds_to_kg(pounds):
    return pounds/2.205


def zeopoxa_cycling_met_units(speed):
    return (0.561*speed) + 0.301


def zeopoxa_calories_per_minute(weight, speed):
    mets = zeopoxa_cycling_met_units(speed)
    weight = _calc_pounds_to_kg(weight)
    return 0.0175*mets*weight


def zeopoxa_calc_total_calories_burned(weight, duration, speed):
    calories_per_minute = zeopoxa_calories_per_minute(weight, speed)
    return calories_per_minute*duration



if __name__ == '__main__':
    print("The Zeopoxa cycling model cannot be run as an executable.")
