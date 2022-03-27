import unittest
import src.calculations.meter_simulator as meter_simulator


class MeterSimulatorTest(unittest.TestCase):
    def setUp(self):
        self.generators = [meter_simulator.simple_meter_generator()
                           for _ in range(100)]
        self.all_test_values = [list(generator)
                                for generator in self.generators]

    def test_value_bounds(self):
        # Creating nudge to allow for minor numerical errors
        nudge = 0.1
        for test_values in self.all_test_values:
            for test_value in test_values:
                self.assertTrue(meter_simulator.METER_VALUES_MINIMUM_WATTS - nudge <= test_value,
                                f"Value is smaller than 0: {test_value}")
                self.assertTrue(test_value <= meter_simulator.METER_VALUES_MAXIMUM_WATTS + nudge,
                                f"Value is bigger than allowed : {test_value}")


if __name__ == '__main__':
    unittest.main()
