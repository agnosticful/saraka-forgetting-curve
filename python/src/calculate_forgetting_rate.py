import math

# Proportionality constant
k = 1.84
K = 1 / k
c = 1.25

def calculate_forgetting_rate(elapsed_minutes):
    return (math.log10(elapsed_minutes))**c * 100 * K / (K * (math.log10(elapsed_minutes))**c + 1)
