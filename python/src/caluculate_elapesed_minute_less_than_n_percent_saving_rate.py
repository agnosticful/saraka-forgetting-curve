import math

def caluculate_elapesed_minute_less_than_n_percent_saving_rate(v):
    return math.pow(10, (math.pow((15.297 / v), 0.5))) * (1.224 * math.pow(10, -4))
