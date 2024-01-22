# Constants for the freezing and boiling points of water
FREEZING_POINT = 0
BOILING_POINT = 100

# This function determines the state of water based on a given temperature,
# using the defined constants for freezing and boiling points.
def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"

# This function categorizes a temperature into "Hot", "Warm", or "Cold".
def categorize_temperature(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    else:
        return "Cold"
