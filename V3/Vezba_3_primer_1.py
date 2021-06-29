import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

# Definisanje diskretnog signala
x = np.zeros(16)
x[: 8] = np.ones(8)
# Računanje spektra signala x
# u 16 i 64 tačke
X1 = fft(x)
X2 = fft(x, 64)
#Crtanje signala
plt.subplot(3, 1, 1)
plt.stem(range(len(x)), x)
plt.title('Diskretni signal x[n]')
plt.subplot(3, 1, 2)
plt.stem(range(len(X1)), np.abs(X1))
plt.title('Amplitudski spektar |X[k]| za N = 16')
plt.subplot(3, 1, 3)
plt.stem(range(len(X2)), np.abs(X2))
plt.title('Amplitudski spektar |X[k]| za N = 64')
plt.show()


# Definisanje diskretnog signala
x = np.zeros(16)
x[: 8] = np.ones(8)
# Računanje spektra signala x
# u 16 i 64 tačke
X1 = fftshift(fft(x))
X2 = fftshift(fft(x, 64))
#Crtanje signala
plt.subplot(3, 1, 1)
plt.stem(range(len(x)), x)
plt.title('Diskretni signal x[n]')
plt.subplot(3, 1, 2)
plt.stem(range(len(X1)), np.abs(X1))
plt.title('Amplitudski spektar |X[k]| za N = 16, prirodni redosled')
plt.subplot(3, 1, 3)
plt.stem(range(len(X2)), np.abs(X2))
plt.title('Amplitudski spektar |X[k]| za N = 64, prirodni redosled')
plt.show()