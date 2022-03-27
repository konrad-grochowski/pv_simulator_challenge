import time
import os
import pickle
import numpy as np
from calculations.timestamp import simple_timestamp_generator, TIMESTAMP_STEP
from calculations.meter_simulator import simple_meter_generator
from shared.meter_output import MeterOutput


def send_meter_values(channel, queue):
    """
    Function publishes serialized object containing timestamp and meter value.
    Timestamp value is number of seconds from midnight.
    The real simulation speed is multiplied by the value
    contained in METER_SENDING_SPEED variable.

    """
    sending_speed = float(os.environ["METER_SENDING_SPEED"])
    timestamp_generator = simple_timestamp_generator()
    meter_generator = simple_meter_generator()
    for timestamp_seconds, meter_value in zip(timestamp_generator, meter_generator):
        meter_output = MeterOutput(timestamp_seconds, meter_value)
        body = pickle.dumps(meter_output)
        channel.basic_publish(exchange='',
                              routing_key=queue,
                              body=body)

        time.sleep(TIMESTAMP_STEP / sending_speed)
