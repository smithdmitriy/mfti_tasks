import numpy as np

def foo_log(x: float):
    base_of_the_logarithm = 1 + x ** 2
    log_number = (np.e ** (1 / (np.sin(x) + 1))) / (5 / 4 + (1 / x ** 15))
    logarithm = np.log(log_number) / np.log(base_of_the_logarithm)
    return logarithm

x = float(input())
print('{0:.08f}'.format(foo_log(x)))
