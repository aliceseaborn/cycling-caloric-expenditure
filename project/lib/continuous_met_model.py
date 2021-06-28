#!/usr/bin/env python
"""Uses the continuous MET model to calculate caloric consumption.
"""

import numpy as np

__author__ = "Alice Seaborn"

__version__ = "0.0.0"
__maintainer__ = "Alice Seaborn"
__email__ = "seaborn.dev@gmail.com"
__status__ = "Prototype"


def _calc_pounds_to_kg(pounds):
    return pounds/2.205


def _coefficients():
    return np.array([3.19343066e-03, -6.25952515e-02,
                     5.62785754e-01, 3.98022780e+00])


def cmet_cycling_met_units(speed):
    """
    Calculates the MET units based on the provided average
    speed throughout the workout. Uses a third-order MET
    polynomial. Assumes speed is provided in miles per hour.
    """
    polynomial = np.poly1d(_coefficients())
    return polynomial(speed)


def cmet_calories_per_minute(weight, speed):
    """
    Calculates the calories burned per minute according to 
    the workout parameters. Uses a third-order MET polynomial.
    Assumes weight is provided in kilograms and the speed is
    provided in miles per hour.
    """
    mets = cmet_cycling_met_units(speed)
    weight = _calc_pounds_to_kg(weight)
    return 0.0175*mets*weight


def cmet_calc_total_calories_burned(weight, duration, speed):
    """
    Calculates the total caloric expenditure of a cycling
    workout based on the parameters provided. Uses a third-
    order MET polynomial. Assumes weight is provided in
    pounds, duration in minutes, speed in miles per hour.
    """
    calories_per_minute = cmet_calories_per_minute(weight, speed)
    return calories_per_minute*duration


if __name__ == '__main__':
    print("The continuous cycling model cannot be run as an executable.")
