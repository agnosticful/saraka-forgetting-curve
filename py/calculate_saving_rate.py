import math

# Proportionality constant
k = 1.84
K = 1 / k
c = 1.25

def calculate_saving_rate(elapsed_minutes):
    return 100 * k / ((math.log(elapsed_minutes))**c + k)