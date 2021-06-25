import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, lfilter

b = [0.4785, 0.31518, 0.019508, -0.099511, -0.018267]
a = [1, -3.614, 5.0702, -3.2616, 0.81451]
n = np.array(range(100))
u = (5 * n - 7) * ((0.9) ** n) * np.cos(2 * np.pi * 1000 / 10000 * n)
y1 = lfilter(b, a, u)
delta_impuls = np.zeros(100)
delta_impuls[0] = 1
g = lfilter(b, a, delta_impuls)

y2 = convolve(g, u)
plt.subplot(2, 1, 1)
plt.stem(n, u)
plt.title('Ulazni signal')
plt.subplot(2, 1, 2)
plt.stem(n, g)
plt.title('Impulsni odziv')
plt.show()

plt.subplot(3, 1, 1)
plt.stem(n, y1)
plt.title('Odziv sistem racunat direktno')
plt.subplot(3, 1, 2)
plt.stem(n, y2[: 100])
plt.title('Odziv sistema racunat pomocu konvolucije')
plt.subplot(3, 1, 3)
plt.stem(n, y1 - y2[: 100])
plt.title('Greska')
plt.show()
    