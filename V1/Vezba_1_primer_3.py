import numpy as np
import matplotlib.pyplot as plt

# Definisanje trajanja intervala na kojem se posmatra signal u sekundama
Tmax = 0.02
# Definisanje ucestanosti na kojima se nalaze komponente u signalu
fk = [100, 1500, 2500]
# Definisanje amplituda prisutnih komponenti 
Ak = np.array([10, 4, 3])
# Definisanje kontinualnog signala, trajanja 5 ms
tk = np.arange(0, Tmax, 0.00001)
Xk = Ak[0] * np.cos(2 * np.pi * fk[0] * tk) - Ak[1] * np.cos(2 * np.pi * fk[1] * tk) + Ak[2] * np.cos(2 * np.pi * fk[2] * tk)
# Odredjivanje snage pojedinih komponenti prisutnih u signalu 
Pk = Ak * (Ak / 2)
# Ukupna snaga signala Xk 
Ptotal = np.sum(Pk)
# Procenat snage koja otpada na pojedine komponente
Pperc = Pk / Ptotal
print(Pperc)

# Obzirom da su procenti ukupne snage po pojedinim komponentama u ovom 
# slucaju 80%, 12.8%, 7.2%, komponenta na ucestanosti f=2500 Hz nosi manje 
# od 10% ukupne snage pa je komponenta na najvisoj ucestanosti koja pri tome 
# nosi vise od 10% ukupne snage ona na 1500 Hz

fmax = 1500
# Definisanje ucestanosti odabiranja
fs = 2 * fmax
Ts = 1 / fs
# Formiranje diskretnog signala
td = np.arange(0, Tmax, Ts)
Xd = Ak[0] * np.cos(2 * np.pi * fk[0] * td) - Ak[1] * np.cos(2 * np.pi * fk[1] * td) + Ak[2] * np.cos(2 * np.pi * fk[2] * td)
# Crtanje kontinualnog signala
plt.subplot(2, 1, 1)
plt.plot(tk, Xk)
plt.title('Kontinualni signal') # Imenovanje grafika
plt.xlabel('Vreme') # Imenovanje x - ose
# Crtanje diskretnog signala
plt.subplot(2, 1, 2)
plt.stem(range(td.shape[0]), Xd)
plt.title('Diskretni signal signal') # Imenovanje grafika
plt.xlabel('Odbirci') # Imenovanje x - ose

plt.show()
