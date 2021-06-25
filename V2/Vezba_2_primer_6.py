import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, lfilter


b = [0.4785, 0.31518, 0.019508, -0.099511, -0.018267]
a = [1, -3.614, 5.0702, -3.2616, 0.81451]
n = np.array(range(100))
u = (5 * n - 7) * ((0.9) ** n) * np.cos(2 * np.pi * 1000 / 10000 * n)
y1 = lfilter(b, a, u)

greska = np.zeros(131)
y2 = np.zeros((131, 1000))
for k in range(20, 151):
    
    delta_impuls = np.zeros(k + 1)
    delta_impuls[0] = 1
    g = lfilter(b, a, delta_impuls)
    temp = convolve(g, u)
    y2[k - 20, : temp.shape[0] + 150 - k] = np.concatenate((temp, np.zeros(150 - k)))
    greska[k - 20] = np.sum(np.abs(y1 - y2[k - 20, : 100])) / 100

plt.plot(range(20, 151), greska)
plt.title('Prosecna greska')
plt.xlabel('Trajanje impulsnog odziva')
plt.show()

plt.subplot(4, 1, 1)
plt.stem(n, y1)
plt.title('Odziv sistema racunat direktno')
plt.subplot(4, 1, 2)
plt.stem(n, y2[0, : 100])
plt.title('Odziv sistema racunat na osnovu impulsnog odziva duzine 20 odbiraka')
plt.subplot(4, 1, 3)
plt.stem(n, y2[30, : 100])
plt.title('Odziv sistema racunat na osnovu impulsnog odziva duzine 50 odbiraka')
plt.subplot(4, 1, 4)
plt.stem(n, y2[80, : 100])
plt.title('Odziv sistema racunat na osnovu impulsnog odziva duzine 100 odbiraka')
plt.show()

