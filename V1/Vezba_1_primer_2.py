import numpy as np
import matplotlib.pyplot as plt

# Definisanje trajanja intervala na kojem se posmatra signal u sekundama
Tmax = 0.02
# Definisanje ucestanosti na kojima se nalaze komponente u signalu 
fk = [100, 1500, 2500]
# Definisanje kontinualnog signala, trajanja 5 ms
tk = np.arange(0, Tmax, 0.00001)
Xk = 10 * np.cos(2 * np.pi * fk[0] * tk) - 5 * np.cos(2 * np.pi * fk[1] * tk) + 7 * np.sin(2 * np.pi * fk[2] * tk)

# Odredjivanje maksimalne ucestanosti koja je prisutna u signalu 
fk_max = max(fk)
# Definisanje ucestanosti odabiranja     
fs = 2 * fk_max
Ts = 1 / fs
# Formiranje diskretnog signala 
td = np.arange(0, Tmax, Ts)
Xd = 10 * np.cos(2 * np.pi * fk[0] * td) - 5 * np.cos(2 * np.pi * fk[1] * td) + 7 * np.sin(2 * np.pi * fk[2] * td)
# Crtanje kontinualnog signala
plt.subplot(2, 1, 1)
plt.plot(tk, Xk, color = 'black')
plt.ylim([-25, 25]) # ogranici opseg y-ose
plt.title('Kontinualni signal') # daj ime grafiku
plt.xlabel('Vreme') # komentarisi prirodu x - ose
# Crtanje diskretnog signala
plt.subplot(2, 1, 2)
plt.stem(range(td.shape[0]), Xd)
plt.ylim([-25, 25]) # ogranici opseg y - ose
plt.title('Diskretni signal') # daj ime grafiku
plt.xlabel('Odbirci') # komentarisi prirodu x - ose

plt.show()


