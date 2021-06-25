import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

a = np.zeros(15)
b = np.zeros(15)
a[5 : 10] = np.ones(5)
b[4 : 11] = np.ones(7)
n = range(15)
c = n
plt.subplot(3, 1, 1)
plt.stem(n, a)
plt.title('Signal a[n]')
plt.subplot(3, 1, 2)
plt.stem(n, b)
plt.title('Signal b[n]')
plt.subplot(3, 1, 3)
plt.stem(n, c)
plt.title('Signal c[n]')
plt.show()

w1 = convolve(a, b)
w2 = convolve(b, a)
plt.subplot(2, 1, 1)
plt.stem(range(len(w1)), w1)
plt.title('a[n] * b[n]')
plt.subplot(2, 1, 2)
plt.stem(range(len(w2)), w2)
plt.title('b[n] * a[n]')
plt.show()

t1 = convolve(b, c)
t2 = convolve(a, b)
w1 = convolve(a, t1)
w2 = convolve(t2, c)
plt.subplot(2, 1, 1)
plt.stem(range(len(w1)), w1)
plt.title('a[n] * (b[n] * c[n])')
plt.subplot(2, 1, 2)
plt.stem(range(len(w2)), w2)
plt.title('(b[n] * a[n]) * c[n]')
plt.show()

w1 = convolve(a, b + c)
w2 = convolve(a, b) + convolve(a, c)
plt.subplot(2, 1, 1)
plt.stem(range(len(w1)), w1)
plt.title('a[n] * (b[n] + c[n])')
plt.subplot(2, 1, 2)
plt.stem(range(len(w2)), w2)
plt.title('a[n] * b[n] + a[n] * c[n]')
plt.show()

t1 = convolve(a, b)
w1 = np.zeros(t1.shape[0])
w1[1 :] = t1[: -1]
temp = np.zeros(a.shape[0])
temp[1 :] = a[: -1]
w2 = convolve(temp, b)
temp = np.zeros(a.shape[0])
temp[1 :] = b[: -1]
w3 = convolve(a, temp)
plt.subplot(3, 1, 1)
plt.stem(range(len(w1)), w1)
plt.title('E ** (-1)(a[n] * b[n])')
plt.subplot(3, 1, 2)
plt.stem(range(len(w2)), w2)
plt.title('(E ** (-1) a[n]) * b[n]')
plt.subplot(3, 1, 3)
plt.stem(range(len(w3)), w3)
plt.title('a[n] * (E ** (-1) b[n])')
plt.show()

delta_impuls = np.zeros(15)
delta_impuls[0] = 1
w1 = convolve(a, delta_impuls)
plt.subplot(2, 1, 1)
temp = np.zeros(a.shape[0] + 14)
temp[: a.shape[0]] = a
plt.stem(range(len(temp)), temp)
plt.title('a[n]')
plt.subplot(2, 1, 2)
plt.stem(range(len(w1)), w1)
plt.title('a[n] * delta[n]')
plt.show()




