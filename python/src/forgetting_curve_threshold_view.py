import numpy as np
from matplotlib import pyplot

from calculate_saving_rate import calculate_saving_rate as cal_saving_rate

def forgetting_curve_threshold_view(threshold, times):

    pyplot.title('Forgetting Curve')
    pyplot.xlabel('minute (m)')
    pyplot.ylabel('Forgetting Rate(%)')
    pyplot.xscale("log")

    next_starting_x = 1

    for _ in range(times):

        # x: range(1, ?, 1)
        minutes = []

        # y: 
        saving_rate_each_minute = []

        i = next_starting_x

        saving_rate = cal_saving_rate(i)

        while True:
            saving_rate = 100 - saving_rate + cal_saving_rate(i)

            if saving_rate < threshold:
                break

            saving_rate_each_minute.append(saving_rate)

            minutes.append(i)

            i += 1

        pyplot.plot(minutes, saving_rate_each_minute, "r--")

        next_starting_x = i - 1

    pyplot.show()