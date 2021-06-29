import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import blackman, hamming, hann, kaiser, triang

# Broj tacaka u kojima se racuna DFT
N = 128
n = np.array(range(N))
# Definisanje signala ciji spektar racunamo
x1 = 10000 * np.cos(2 * np.pi * 10 * n / N) + 100 * np.cos(2 * np.pi * 16 * n / N)
# Odredjivanje amplitudske karakteristike
X1 = 2 * np.abs(fft(x1)) / N
# Izracunavanje karakteristike u dB
X1 = 20 * np.log10(X1)
# Crtanje karakteristike
plt.subplot(2, 2, 1)
plt.stem(n, X1)
plt.title('Spektar signala x1[n]')
plt.axis([0, 32, 0, 80])
# Modifikacija signala x1[n] tako da se ucestanost prve komponente nalazi
# izmedju dve tacke u kojima racunamo DFT
x2 = 10000 * np.cos(2 * np.pi * 10.5 * n / N) + 100 * np.cos(2 * np.pi * 16 * n / N)
# Odredjivanje amplitudske karakteristike
X2 = 2 * np.abs(fft(x2)) / N
X2 = 20 * np.log10(X2)
# Crtanje karakteristike
plt.subplot(2, 2, 2)
plt.stem(n, X2)
plt.title('Spektar signala x2[n]')
plt.axis([0, 32, 0, 80])
# Trougaoni prozor
w = triang(N)
x3 = x2 * w
X3 = 2 * np.abs(fft(x3)) / N
X3 = 20 * np.log10(X3)
plt.subplot(2, 2, 3)
plt.stem(n, X3)
plt.title('Trougaoni prozor')
plt.axis([0, 32, 0, 80])
# Hanov prozor
w = hann(N)
x4 = x2 * w
X4 = 2 * np.abs(fft(x4)) / N
X4 = 20 * np.log10(X4)
plt.subplot(2, 2, 4)
plt.stem(n, X4)
plt.title('Hanov prozor')
plt.axis([0, 32, 0, 80])
plt.show()
# Hemingov prozor
w = hamming(N)
x5 = x2 * w
X5 = 2 * np.abs(fft(x5)) / N
X5 = 20 * np.log10(X5)
plt.subplot(2, 2, 1)
plt.stem(n, X5)
plt.title('Hemingov prozor')
plt.axis([0, 32, 0, 80])
# Blekmanov prozor
w = blackman(N)
x6 = x2 * w
X6 = 2 * np.abs(fft(x6)) / N
X6 = 20 * np.log10(X6)
plt.subplot(2, 2, 2)
plt.stem(n, X6)
plt.title('Blekmanov prozor')
plt.axis([0, 32, 0, 80])
# Kajzerov prozor za beta = 4
w = kaiser(N, 4)
x7 = x2 * w
X7 = 2 * np.abs(fft(x7)) / N
X7 = 20 * np.log10(X7)
plt.subplot(2, 2, 3)
plt.stem(n, X7)
plt.title('Kajzerov prozor za \u03B2 = 4')
plt.axis([0, 32, 0, 80])
# Kajzerov prozor za beta = 9
w = kaiser(N, 9)
x8 = x2 * w
X8 = 2 * np.abs(fft(x8)) / N
X8 = 20 * np.log10(X8)
plt.subplot(2, 2, 4)
plt.stem(n, X8)
plt.title('Kajzerov prozor za \u03B2 = 9')
plt.axis([0, 32, 0, 80])
plt.show()

