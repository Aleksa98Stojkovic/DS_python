import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, lfiltic

b = [4]
a = [1, -9/5, 81/100]
n = np.array(range(100))
u = 0.5 ** n

yi = [-20/9, -600/81]
ui = [0, 0]
zi = lfiltic(b, a, yi, ui)
y =  lfilter(b, a, u, zi = zi)

ya = 2 * ((9 / 10) ** n) + 4 * n * ((9 / 10) ** n) - 2.25 * ((9 / 10) ** n) + 9 * n * ((9 / 10) ** n) + 25 / 4 * (0.5 ** n)
plt.subplot(3, 1, 1)
plt.stem(n, ya)
plt.title('Analiticko resenje')
plt.subplot(3, 1, 2)
plt.stem(n, y[0])
plt.title('Numericko resenje')
plt.subplot(3, 1, 3)
plt.stem(n, ya - y[0])
plt.title('Greska')
plt.show()
