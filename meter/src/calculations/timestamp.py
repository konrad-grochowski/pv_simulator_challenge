SECONDS_IN_DAY = 60 * 60 * 24
TIMESTAMP_STEP = 5
NUMBER_OF_VALUES = SECONDS_IN_DAY // TIMESTAMP_STEP


def simple_timestamp_generator():
    return range(0, SECONDS_IN_DAY, TIMESTAMP_STEP)
