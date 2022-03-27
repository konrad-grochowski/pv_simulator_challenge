import time
import os
import pickle
from shared.meter_output import MeterOutput


SECONDS_IN_DAY = 60 * 60 * 24
TIMESTAMP_STEP = 25


def simple_timestamp_generator():
    return range(0, SECONDS_IN_DAY, TIMESTAMP_STEP)


def simple_meter_generator():
    for i in range(10000):
        yield i
    return


def send_meter_values(channel, queue):
    """
    Function publishes serialized object containing timestamp and meter value.
    Timestamp value is number of seconds from midnight.
    Function reads METER_SENDING_SPEED environment variable
    The timeout in between sent messages equals to:
        TIMESTAMP_STEP / sending_speed

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

        print(f"Timestamp: {timestamp_seconds} and meter value: {meter_value}"
              " have been sent to the broker")
        time.sleep(TIMESTAMP_STEP / sending_speed)
