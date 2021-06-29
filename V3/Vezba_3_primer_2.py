import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift


n = np.array(range(128))

# Definisanje dva kompleksna eksponencijalna signala duzine 128 odbiraka
fo1 = 21 / 128
x1 = np.exp(1j * 2 * np.pi * fo1 * n)
fo2 = 21 / 127
x2 = np.exp(1j * 2 * np.pi * fo2 * n)

# Spektri oba signala
X1 = fft(x1)
X2 = fft(x2)

# Crtanje amplitudskih spektara u prirodnom redosledu
plt.subplot(2, 1, 1)
plt.stem(n, fftshift(np.abs(X1)))
plt.subplot(2, 1, 2)
plt.stem(n, fftshift(np.abs(X2)))
plt.show()