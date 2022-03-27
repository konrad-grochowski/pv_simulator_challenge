import pickle
import time
from datetime import datetime
# import matplotlib.pyplot as plt
import numpy as np
from calculations import input_scaler, simulating_function
from shared.meter_output import MeterOutput


def write_to_file(logs_timestamp, meter_timestamp, meter_value, pv_simulator_value):
    """
    Function writing measured values in the csv file containing the current date.
    Arguments:
        logs_timestamp: string used to create and append to a file containing measured values;
        meter_timestamp: timestamp which comes with the meter_value;
        meter_value: Value received from the meter;
        pv_simulator_value: Value generated by the PV simulating function;
    """
    with open(f"./logs/{logs_timestamp}_logs.csv", "a+") as output_file:
        values_sum = meter_value + pv_simulator_value
        new_content = f"{meter_timestamp},{meter_value},{pv_simulator_value},{values_sum}\n"
        output_file.write(new_content)


def callback(body, logs_timestamp):
    """
    Function serves as a callback for message arrivals.
    Uses pickle libary to deserialize the message.
    Function used to simulate the PV power generation is based on beta distribution PDF,
    so the arguments are scaled to fit in 0.0-1.0 range.
    Arguments:
        body: serialized message from meter simulator, contains timestamp and meter value;
        logs_timestamp: string used to create and append to a file containing measured values;

    """
    meter_output = pickle.loads(body)
    scaled_input = input_scaler.scale_input(meter_output.timestamp_seconds)
    pv_simulator_value = simulating_function.get_value(scaled_input)
    write_to_file(logs_timestamp, meter_output.timestamp_seconds,
                  meter_output.meter_value, pv_simulator_value)
    print(f"input:{scaled_input}, value: {pv_simulator_value}")
    return scaled_input, pv_simulator_value


def create_callback(logs_timestamp):
    """
    Function puts callback function into a wrapper, 
    which allows changing the signature.
    Arguments:
        logs_timestamp: string wchich preserves the timestamp 
            used to name file storing the power values;

    """
    def callback_wrapper(channel, method, properties, body):
        return callback(body, logs_timestamp)
    return callback_wrapper

# print(callback(6*HOUR_IN_SECONDS))
# xs = []
# ys = []
# for x in np.arange(DAILY_ENERGY_START, DAILY_ENERGY_STOP, 100):
#     x, y = callback(x)
#     xs.append(x)
#     ys.append(y)

# plt.plot(xs, ys)
# plt.show()