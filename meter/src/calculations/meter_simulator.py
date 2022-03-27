import numpy as np
"""
Package provides simulated meter values. 
Normal distribution is used to create delta values to subsequent mater values.
Created values are rescaled to fit in the range described by
METER_VALUES_MINIMUM_WATTS and METER_VALUES_MAXIMUM_WATTS values.
"""

SECONDS_IN_DAY = 60 * 60 * 24
TIMESTAMP_STEP = 5
NUMBER_OF_VALUES = SECONDS_IN_DAY // TIMESTAMP_STEP


METER_VALUES_MINIMUM_WATTS = 0
METER_VALUES_MAXIMUM_WATTS = 9000
METER_VALUES_RANGE_WATTS = METER_VALUES_MAXIMUM_WATTS - METER_VALUES_MINIMUM_WATTS

MU = 0
SIGMA = 50


def simple_meter_generator():
    normal_values = np.random.normal(MU, SIGMA, NUMBER_OF_VALUES)
    current_value = 0
    meter_values = [current_value]
    for normal_value in normal_values:
        current_value += normal_value
        meter_values.append(current_value)
    meter_values = np.array(meter_values)
    # Adding bias to set the function minimum to 0
    meter_values -= np.min(meter_values)
    # Scaling the values to fit into range
    meter_values *= METER_VALUES_RANGE_WATTS / np.max(meter_values)
    # Adding bias again to match minimum and maximum
    meter_values += METER_VALUES_MINIMUM_WATTS

    for value in meter_values:
        yield value
