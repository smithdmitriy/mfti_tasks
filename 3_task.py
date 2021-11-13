import numpy as np
import matplotlib.pyplot as plt


def foo_3(x):
    base_of_the_logarithm = 1 + np.tan(1 / (1 + np.sin(x) ** 2))
    log_number = (x ** 2 + 1) * np.exp(- np.abs(x) / 10)
    logarithm = np.log(log_number) / np.log(base_of_the_logarithm)
    return logarithm


x = np.arange(-250, 250, 0.001)
plt.figure(figsize=(14, 7))
plt.plot(x, foo_3(x), lw=0.5)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.title(r'$\sin(x)$') #TODO write title jf the foo_3
plt.minorticks_on()
plt.grid(which='major',
         color='k',
         linewidth=0.5)
plt.grid(which='minor',
         color='g',
         linewidth=0.3,
         linestyle=':')
plt.show()
