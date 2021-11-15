import numpy as np
import matplotlib.pyplot as plt


def weierstrass_f(a, b, x):
    fx = np.array([])
    i = 0
    while i <= len(x) - 1:
        j = 0
        sigm = 0
        while j <= 10:
            sigm += b ** j * np.cos(a ** j * np.pi * x[i])
            j += 1
        fx = np.append(fx, [sigm])
        i += 1
    return (fx)


start = -2
stop = 2
step = 0.0001
a = 3
b = 0.5
x = np.arange(start, stop, step)
plt.figure(figsize=(14, 7))
plt.plot(x, weierstrass_f(a, b, x), lw=0.3)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.title(r'Weierstrass function', fontsize=20)
plt.minorticks_on()
plt.grid(which='major',
         color='k',
         linewidth=0.5)
plt.grid(which='minor',
         color='g',
         linewidth=0.3,
         linestyle=':')
plt.show()
