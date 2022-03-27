import unittest
import numpy as np
import src.calculations.input_scaler as input_scaler


class InputScalerTest(unittest.TestCase):
    def setUp(self):
        day_in_seconds = 24*60*60
        step_seconds = 5
        self.test_arguments = np.arange(0, day_in_seconds, step_seconds)

    def test_times_before_power_range(self):
        time_before_power_range = 4 * input_scaler.HOUR_IN_SECONDS
        self.assertEqual(input_scaler.scale_input(time_before_power_range), 0)

    def test_times_after_power_range(self):
        time_after_power_range = 22 * input_scaler.HOUR_IN_SECONDS
        self.assertEqual(input_scaler.scale_input(time_after_power_range), 0)

    def test_mapping_linearity(self):
        first_quarter = input_scaler.DAILY_POWER_START + \
            input_scaler.DAILY_POWER_RANGE / 4
        second_quarter = input_scaler.DAILY_POWER_START + \
            2 * input_scaler.DAILY_POWER_RANGE / 4
        third_quarter = input_scaler.DAILY_POWER_START + \
            3 * input_scaler.DAILY_POWER_RANGE / 4
        fourth_quarter = input_scaler.DAILY_POWER_START + input_scaler.DAILY_POWER_RANGE
        self.assertEqual(input_scaler.scale_input(first_quarter), 0.25)
        self.assertEqual(input_scaler.scale_input(second_quarter), 0.50)
        self.assertEqual(input_scaler.scale_input(third_quarter), 0.75)
        self.assertEqual(input_scaler.scale_input(fourth_quarter), 1.00)


if __name__ == '__main__':
    unittest.main()
