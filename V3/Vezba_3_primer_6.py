import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Opis LVN DS pomocu operatorskih polinoma
a = [1, -1.5035, 0.64]
b = [1, -1.9002, 0.998]

# Definisanje ulaznog signala duzine 64 odbirka
n = np.array(range(64))
fs = 8000
f1 = 400
f2 = 800
u = 4 * np.cos(2 * np.pi * f1 * n / fs) + np.cos(2 * np.pi * f2 * n / fs)

plt.stem(n, u)
plt.title('Ulaz')
plt.show()

# Izracunavanje odziva u vremenskom domenu
y1 = lfilter(b, a, u)

plt.subplot(3, 1, 1)
plt.stem(n, y1)
plt.title('Izlaz racunat pomocu funkcije lfilter')

# Vrednost amplitudske i fazne karakteristike na ucestanosti f1
w = 2 * np.pi * f1 / fs
# Prenosna karakteristika sistema u frekvencijskom domenu
G = (1 - 1.9002 * np.exp(-1j * w) + 0.998 * np.exp(-1j * 2 * w)) / (1 - 1.5035 * np.exp(-1j * w) + 0.64 * np.exp(-1j * 2 * w))
# Amplitudska karakteristika
A_f1 = np.abs(G)
# Fazna karakteristika
F_f1 = np.angle(G)

# Vrednost amplitudske i fazne karakteristike na ucestanosti f2
w = 2 * np.pi * f2 / fs
# Prenosna karakteristika sistema u frekvencijskom domenu
G = (1 - 1.9002 * np.exp(-1j * w) + 0.998 * np.exp(-1j * 2 * w)) / (1 - 1.5035 * np.exp(-1j * w) + 0.64 * np.exp(-1j * 2 * w))
# Amplitudska karakteristika
A_f2 = np.abs(G)
# Fazna karakteristika
F_f2 = np.angle(G)

# Izracunavanje odziva na osnovu modifikacije amplitude i faze komponenti
y2 = A_f1 * 4 * np.cos(2 * np.pi * f1 / fs * n + F_f1) + A_f2 * np.cos(2 * np.pi * f2 / fs * n + F_f2) 
plt.subplot(3, 1, 2)
plt.stem(n, y2)
plt.title('Izlaz racunat modifikacijom amplitude i faze prisutnih komponenti')
# Greska izmedju dva nacina racunanja odziva
plt.subplot(3, 1, 3)
plt.stem(n, y1 - y2)
plt.title('Greska izmedju dva pristupa')





