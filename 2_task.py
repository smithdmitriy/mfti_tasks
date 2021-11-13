import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 4, 0.001)
plt.plot(x, x ** 2 - x - 6)
plt.minorticks_on()
plt.grid(which='major',
         color='k',
         linewidth=1)
plt.grid(which='minor',
         color='k',
         linestyle=':')
plt.show()
