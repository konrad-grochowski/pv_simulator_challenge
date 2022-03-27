from scipy.stats import beta

"""
This package generates values of the PV simulator.
Beta distribution PDF is used to simulate the values.

"""

ALPHA = 5.0
BETA = 3.5
MODE = (ALPHA - 1) / (ALPHA + BETA - 2)
MAXIMUM_BETA_PDF_VALUE = beta.pdf(MODE, ALPHA, BETA)

MAXIMUM_PV_SIMULATOR_VALUE_WATTS = 3250.0

# Variable used to scale the function properly, so that the maximum is 3250 watts.
SCALING_COEFF = MAXIMUM_PV_SIMULATOR_VALUE_WATTS / MAXIMUM_BETA_PDF_VALUE


def get_value(argument):
    return beta.pdf(argument, ALPHA, BETA) * SCALING_COEFF
