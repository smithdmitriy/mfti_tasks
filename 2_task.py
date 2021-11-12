import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.001)
plt.plot(x, x**2 - x - 6)
plt.grid(True)
plt.show()