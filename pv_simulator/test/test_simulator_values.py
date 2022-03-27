import unittest
import numpy as np
import src.calculations.simulating_function as sim_fnc


class SimulatorValuesTest(unittest.TestCase):
    def setUp(self):
        self.test_arguments = np.arange(0.0, 1.0, 0.0001)
        self.test_values = [sim_fnc.get_value(
            argument) for argument in self.test_arguments]

    def test_value_bounds(self):
        for value in self.test_values:
            self.assertTrue(0.0 <= sim_fnc.get_value(value) <= 3250.0)

    

if __name__ == '__main__':
    unittest.main()
