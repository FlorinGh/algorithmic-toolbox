# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    ''' capacity is a positive integer
    weights and values are lists of integers
    '''
    # compute values per unit
    values_unit = []
    for i in range(len(values)):
        values_unit.append(values[i]/weights[i])
    
    # sort weights, total values and values per unit based on values per unit
    values = [x for _, x in sorted(zip(values_unit,values), reverse=True)]
    weights = [x for _, x in sorted(zip(values_unit,weights), reverse=True)]
    values_unit.sort(reverse=True)
    
    # pass through the lists and fill the capacity based on the available values
    value = 0.0
    for i in range(len(values)):
        if capacity == 0:
            return value
        units = min(weights[i], capacity)
        value += units * values_unit[i]
        capacity -= units
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
