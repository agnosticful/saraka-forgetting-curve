import numpy as np
from matplotlib import pyplot

from calculate_saving_rate import calculate_saving_rate as cal_saving_rate

pyplot.title('Forgetting Curve')
pyplot.xlabel('minute (m)')
pyplot.ylabel('Forgetting Rate(%)')
pyplot.xscale("log")

range_of_min = [k for k in range(10**5)]

for j in range(5):
    curve_data_first = cal_saving_rate(10**j)
    
    value_each_min = [(100 - curve_data_first + cal_saving_rate(i)) for i in range_of_min[10**j:]]
    pyplot.plot(range_of_min[10**j:], value_each_min, "r--")

    print((range_of_min[10**j:])[:5])
    print(value_each_min[:5])

pyplot.show()