import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 2*np.pi, 0.001)
r = 4
plt.plot(r*np.sin(t), r*np.cos(t+np.pi), lw=3)
plt.axis('equal')
plt.show()