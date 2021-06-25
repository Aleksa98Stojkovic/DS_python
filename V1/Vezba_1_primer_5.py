import numpy as np
import matplotlib.pyplot as plt

# Diskretno vreme
n = range(100)
# Definisanje dva diskretna signala
x1 = np.zeros(len(n))
x1[20 :] = np.ones(x1[20 :].shape[0])
x2 = np.zeros(len(n))
x2[60 :] = np.ones(x1[60 :].shape[0])

x3 = x1 + x2 # Zbir dva diskretna signala
x4 = x1 - x2 # Razlika dva diskretna signala

# Crtanje diskretnih signala
plt.subplot(2, 2, 1)
plt.stem(n, x1)
plt.title('x1[n]')

plt.subplot(2, 2, 2)
plt.stem(n, x2)
plt.title('x2[n]')

plt.subplot(2, 2, 3)
plt.stem(n, x3)
plt.title('x3[n] = x1[n] + x2[n]')

plt.subplot(2, 2, 4)
plt.stem(n, x4)
plt.title('x4[n] = x1[n] - x2[n]')

plt.show()


fs = 12000 # Frekvencija odabiranja
# Diskretno vreme
n = np.array(range(200))
# Amplituda prvog prostoperiodicnog signala
A1 = 1 
# Frekvencija prvog prostoperiodicnog signala
fo1 = 50
# Definisanje prvog prostoperiodicnog signala
x1 = A1 * np.cos(2 * np.pi * (fo1 / fs) * n)
# Amplituda drugog prostoperiodicnog signala
A2 = 1
# Frekvencija prvog prostoperiodicnog signala
fo2 = 500
# Definisanje prvog prostoperiodicnog signala
x2 = A2 * np.cos(2 * np.pi * (fo2 / fs) * n)
A = 5
x3 = A * x1 # Proizvod konstante i diskretnog signala
x4 = x1 * x2 # Proizvod dva diskretna signala

# Crtanje signala
plt.subplot(2, 2, 1)
plt.stem(n, x1)
plt.title('x1[n]')

plt.subplot(2, 2, 2)
plt.stem(n, x2)
plt.title('x2[n]')

plt.subplot(2, 2, 3)
plt.stem(n, x3)
plt.title('x3[n] = A * x1[n]')

plt.subplot(2, 2, 4)
plt.stem(n, x4)
plt.title('x4[n] = x1[n] * x2[n]')

plt.show()
