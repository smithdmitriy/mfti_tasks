import numpy as np
import matplotlib.pyplot as plt

y = str(input())
x = np.arange(-10, 10, 0.001)

with plt.xkcd():
    plt.figure(figsize=(14, 7))
    plt.plot(x, eval(y), lw=5)
    plt.xlabel(r'$x$', fontsize=20)
    plt.ylabel(r'$f(x)$', fontsize=20)
    plt.title("f(x)= "+ y, fontsize=20)
plt.show()
