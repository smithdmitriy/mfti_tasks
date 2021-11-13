import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.001)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.show()