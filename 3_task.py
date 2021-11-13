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
plt.title(r'$f\left(x \right)=\log _{1+\tan \left(\frac{1}{1+\sin ^{2}\left(x '
          r'\right)} \right)}\left(x^{2}+1\right)\exp \left(-\frac{\left|x '
          r'\right|}{10} \right)$',fontsize=20)
plt.minorticks_on()
plt.grid(which='major',
         color='k',
         linewidth=0.5)
plt.grid(which='minor',
         color='g',
         linewidth=0.3,
         linestyle=':')
plt.show()
