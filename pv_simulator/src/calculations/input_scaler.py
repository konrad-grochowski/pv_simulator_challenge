"""
This package uses the timestamp value that comes from the meter
to create value from 0.0-1.0 range, which fits into beta distribution PDF.
DAILY_POWER_START and DAILY_POWER_STOP values indicate range where the simulating function is used.
This range is mapped into 0.0-1.0 range linearly.W
"""

HOUR_IN_SECONDS = 3600
DAILY_POWER_START = 5 * HOUR_IN_SECONDS
DAILY_POWER_STOP = 20.5 * HOUR_IN_SECONDS
DAILY_POWER_RANGE = DAILY_POWER_STOP - DAILY_POWER_START


def scale_input(seconds_from_midnight):
    if seconds_from_midnight < DAILY_POWER_START \
            or seconds_from_midnight > DAILY_POWER_STOP:
        return 0

    seconds_after_start = seconds_from_midnight - DAILY_POWER_START
    return seconds_after_start / DAILY_POWER_RANGE
