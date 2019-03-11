import math

def forgetting_curve_enhanced(minute):
    if minute == 0:
        return 100
    else:
        return 15.297 / math.pow(math.log10(minute / (1.224 * math.pow(10, -4))), 2)