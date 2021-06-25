import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

b = [1]
a = [1, -1.807, 0.9025]
n = range(100)
delta_impuls = np.zeros(len(n))
delta_impuls[0] = 1
hevisajd = np.ones(len(n))
g = lfilter(b, a, delta_impuls)
i = lfilter(b, a, hevisajd)
plt.subplot(2, 1, 1)
plt.stem(n, g)
plt.title('Impulsni odziv sistema racunat po definiciji')
plt.subplot(2, 1, 2)
plt.stem(n, i)
plt.title('Jedinicni odziv sistema racunat po definiciji')
plt.show()

i_pom = np.zeros(len(n))
i_pom[1 :] = i[0 : 99]
g1 = i - i_pom
i1 = 0


i1 = 0
for k in range(100):
    
    g_pom = np.zeros(len(n))
    g_pom[k : ] = g[0 : len(n) - k]
    i1 += g_pom
    
plt.subplot(2, 1, 1)
plt.stem(n, g1)
plt.title('Impulsni odziv sistema racunat na osnovu jedinicnog odziva')
plt.subplot(2, 1, 2)
plt.stem(n, i1)
plt.title('Jedinicni odziv sistema racunat na onovu impulsnog odziva')
plt.show()

g_delta = g - g1
i_delta = i - i1

plt.subplot(2, 1, 1)
plt.stem(n, g_delta)
plt.title('Impulsni odziv, greska dva pristupa')
plt.subplot(2, 1, 2)
plt.stem(n, i_delta)
plt.title('Jedinicni odziv, greska dva pristupa')
plt.show()