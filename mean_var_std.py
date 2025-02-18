import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("must contain nine numbers.")

    my_array = np.array(list).reshape(3, 3)

    mean = [my_array.mean(axis=0).tolist(), my_array.mean(axis=1).tolist(), my_array.mean()]
    variance = [my_array.var(axis=0).tolist(), my_array.var(axis=1).tolist(), my_array.var()]
    std_value = [my_array.std(axis=0).tolist(), my_array.std(axis=1).tolist(), my_array.std()]
    max_value = [my_array.max(axis=0).tolist(), my_array.max(axis=1).tolist(), my_array.max()]
    min_value = [my_array.min(axis=0).tolist(), my_array.min(axis=1).tolist(), my_array.min()]
    sum_value = [my_array.sum(axis=0).tolist(), my_array.sum(axis=1).tolist(), my_array.sum()]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_value,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }

    return calculations