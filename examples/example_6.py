import numpy as np
import matplotlib.pyplot as plt
plt.subplot(111, polar=True)
phi = np.arange(0, 4*np.pi, 0.001)
rho = phi
plt.plot(phi, rho, lw=5)
plt.show()