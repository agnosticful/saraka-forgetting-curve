from calculate_saving_rate import calculate_saving_rate as cal_saving_rate

def get_interval(threshold, learned_times):
    threshold_reach_point_list = []
    next_starting_x = 1

    for _ in range(learned_times + 1):

        minutes = []

        i = next_starting_x

        first_saving_rate = cal_saving_rate(i)

        while True:
            saving_rate = 100 - first_saving_rate + cal_saving_rate(i)

            if saving_rate < threshold:
                threshold_reach_point_list.append(minutes[-1])
                break

            minutes.append(i)

            i += 1

        next_starting_x = i - 1

    return (threshold_reach_point_list[-1] - threshold_reach_point_list[-2])

print(get_interval(60, 2))
