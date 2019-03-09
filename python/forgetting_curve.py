import numpy as np
import math
from matplotlib import pyplot

# Proportionality constant
k = 1.84
K = 1 / k
c = 1.25
threshold = 60

def calculate_saving_rate(elapsed_minutes):
    return 100 * k / ((math.log(elapsed_minutes))**c + k)

pyplot.title('Forgetting Curve')
pyplot.xlabel('minute (m)')
pyplot.ylabel('Forgetting Rate(%)')
pyplot.xscale("log")

range_of_min = [k for k in range(10**5)]

for j in range(5):
    curve_data_first = calculate_saving_rate(10**j)
    
    value_each_min = [(100 - curve_data_first + calculate_saving_rate(i)) for i in range_of_min[10**j:]]
    pyplot.plot(range_of_min[10**j:], value_each_min, "r--")

    print((range_of_min[10**j:])[:5])
    print(value_each_min[:5])

pyplot.show()