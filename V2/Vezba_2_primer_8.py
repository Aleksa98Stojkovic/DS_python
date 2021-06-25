import numpy as np
import matplotlib.pyplot as plt
from plot_zplane import zplane
from scipy.signal import lfilter


brojilac = [3, -7, 5]
imenilac = [1, -5 / 2, 1]
zo = np.roots(brojilac)
zp = np.roots(imenilac)
k = brojilac[0] / imenilac[0]
print('Nule funkcije prenosa su: \n', zo)
print('Polovi funkcije prenosa su: \n', zp)
print('Pojacanje k je: \n', k)

b = [0.08632, 0.055706, 0.14939, 0.055706, 0.08632]
a = [1, -1.6992, 2.1371, -1.3258, 0.50014]
nule = np.roots(b)
polovi = np.roots(a)
print('Polovi funkcije prenosa su: \n', polovi)

if all(a < 1 for a in np.abs(polovi)):
    print('Sistem je stabilan')
else:
    print('Sistem je nestabilan')

zplane(np.array(b), np.array(a))
delta_impuls = np.zeros(100)
delta_impuls[0] = 1
g = lfilter(b, a, delta_impuls)
plt.stem(range(len(g)), g)
plt.title('Impulsni odziv sistema')
plt.show()

# Za druge vrednosti b i a

b = [0, 1, 3]
a = [1, -3.25, 0.75]
polovi = np.roots(a)
print('Polovi funkcije prenosa su: \n', polovi)
if all(a < 1 for a in np.abs(polovi)):
    print('Sistem je stabilan')
else:
    print('Sistem je nestabilan')

zplane(np.array(b), np.array(a))
delta_impuls = np.zeros(100)
delta_impuls[0] = 1
g = lfilter(b, a, delta_impuls)
plt.stem(range(len(g)), g)
plt.title('Impulsni odziv sistema')
plt.show()