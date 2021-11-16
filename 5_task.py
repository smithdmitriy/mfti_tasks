import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
plt.plot(x, p_f(x), )
plt.plot(x, y, 'o')
plt.errorbar(x, p_f(x), yerr=y - p_f(x))
plt.fill_between(x, p_f(x), y, alpha=0.3)

plt.show()