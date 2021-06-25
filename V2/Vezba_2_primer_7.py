import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

g1 = [0.0057048, 0.012593, -0.0084744, -0.034508, 0.013923, 0.085803, -0.018314,
      -0.31103, 0.52004, -0.31103, -0.018314, 0.085803, 0.013923, -0.034508,
      -0.0084744, 0.012593, 0.0057048]
g2 = [-0.010771, 0.0026215, 0.023095, 0.011271, -0.047517, -0.064009, 0.070764,
      0.30343, 0.42223, 0.30343, 0.070764, -0.064009, -0.047517, 0.011271,
      0.023095, 0.0026215, -0.010771]

plt.subplot(2, 1, 1)
plt.stem(range(len(g1)), g1)
plt.title('Impulsni odziv prvog podsistema')
plt.subplot(2, 1, 2)
plt.stem(range(len(g2)), g2)
plt.title('Impulsni odziv drugog podsistema')

impuls = np.zeros(17)
impuls[0] = 1
pom = convolve(g1, impuls)
g_par1 = convolve(g2, pom)
g_par_ekv = convolve(g1, g2)
g_par2 = convolve(g_par_ekv, impuls)

plt.subplot(3, 1, 1)
plt.stem(range(len(g_par1)), g_par1)
plt.title('Impulsni odziv originalnog sistema')
plt.subplot(3, 1, 2)
plt.stem(range(len(g_par2)), g_par2)
plt.title('Impulsni odziv ekvivalentnog sistema')
plt.subplot(3, 1, 3)
plt.stem(range(len(g_par1)), g_par1 - g_par2)
plt.title('Greska')
plt.show()

pom1 = convolve(g1, impuls)
pom2 = convolve(g2, impuls)
g_red1 = pom1 + pom2
g_red_ekv = np.array(g1) + np.array(g2)
g_red2 = convolve(g_red_ekv, impuls)

plt.subplot(3, 1, 1)
plt.stem(range(len(g_red1)), g_red1)
plt.title('Impulsni odziv originalnog sistema')
plt.subplot(3, 1, 2)
plt.stem(range(len(g_red2)), g_red2)
plt.title('Impulsni odziv ekvivalentnog sistema')
plt.subplot(3, 1, 3)
plt.stem(range(len(g_red1)), g_red1 - g_red2)
plt.title('Greska')
plt.show()