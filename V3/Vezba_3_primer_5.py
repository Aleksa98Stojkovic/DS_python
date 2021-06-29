import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import kaiser

fs = 44100 # Ucestanost odabiranja
f1 = 2000 # Ucestanost prve komponente u spektru
f2 = 3000 # Ucestanost druge komponente u spektru

# Varijanta 1: pravougaoni prozor duzine 256 odbiraka
N = 256
n = np.array(range(N))
x1 = 10000 * np.cos(2 * np.pi * f1 * n / fs) + 100 * np.cos(2 * np.pi * f2 * n / fs)
X1 = 2 * np.abs(fft(x1)) / N
X1 = 20 * np.log10(X1)
plt.subplot(3, 1, 1)
plt.stem(n * (fs / N), X1)
plt.title('Spektar signala x1[n], pravougaoni prozor duzine 256 odbiraka')
plt.axis([0, 4000, 0, 80]) # zumiramo deo spektra od interesa

# Varijanta 2: pravougaoni prozor duzine 2048 odbiraka
N = 2048
n = np.array(range(N))
x1 = 10000 * np.cos(2 * np.pi * f1 * n / fs) + 100 * np.cos(2 * np.pi * f2 * n / fs)
X1 = 2 * np.abs(fft(x1)) / N
X1 = 20 * np.log10(X1)
plt.subplot(3, 1, 2)
plt.stem(n * (fs / N), X1)
plt.title('Spektar signala x1[n], pravougaoni prozor duzine 2048 odbiraka')
plt.axis([0, 4000, 0, 80]) # zumiramo deo spektra od interesa

# Varijanta 3: Kajzerov prozor duzine 256 odbiraka i beta = 9
N = 256
n = np.array(range(N))
x1 = 10000 * np.cos(2 * np.pi * f1 * n / fs) + 100 * np.cos(2 * np.pi * f2 * n / fs)
x1 = x1 * kaiser(N, 9)
X1 = 2 * np.abs(fft(x1)) / N
X1 = 20 * np.log10(X1)
plt.subplot(3, 1, 3)
plt.stem(n * (fs / N), X1)
plt.title('Spektar signala x1[n], Kajzerov prozor duzine 256 odbiraka')
plt.axis([0, 4000, 0, 80]) # zumiramo deo spektra od interesa
plt.show()