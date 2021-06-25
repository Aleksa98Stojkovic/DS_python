import numpy as np
import matplotlib.pyplot as plt

""" Prikaz diskretnog delta impulsa """
# Duzina sekvence
L = 16
# Formiranje Dirakove funkcije, odnosno delta impulsa
delta_impuls = np.zeros(L)
delta_impuls[0] = 1
# Vremnsko kasnjenje
m = 4
#  Formiranje pomerenog delta impulsa za m odbiraka
delta_impuls1 = np.zeros(L)
delta_impuls1[m] = 1
# Crtanje delta impulsa
plt.stem(range(L), delta_impuls)
plt.title('Delta impuls u koordinatnom pocetku')
plt.show()
# Crtanje pomerenog delta impulsa
plt.stem(range(L), delta_impuls1)
plt.title('Delta impuls zakasnjen za m odbiraka')
plt.show()

""" Prikaz diskrene Hevisajdove funkcije """
# Duzina sekvence
L = 64
# Formiranje Hevisajdove funkcije
hevisajd = np.ones(L)
hevisajd[0 : L // 2] = np.zeros(L // 2)
# Crtanje Hevisajda
plt.stem(range(-L // 2, L // 2), hevisajd)
plt.title('Diskrenta Hevisajdova funkcija')
plt.show()

""" Prikaz diskretnog prostoperiodicnog signala """
# Parametri prostoperiodicnog signala
A = 50 # Amplituda
fo = 50 # Frekvencija
ugao = np.pi / 4 # Fazni pomeraj
fs = 8000 # Frekvencija odabiranja
# Diskretno vreme
n = np.array(range(128))
x = A * np.cos(2 * np.pi * (fo / fs) * n + ugao)
# Crtanje diskretnog prostoperiodicnog signala
plt.stem(n, x)
plt.title('Diskretni prostoperiodicni signal')
plt.show()

""" Prikaz osnovnih stepenih funkcija """
osnova1 = -0.9
osnova2 = 1.2
# Diskretno vreme
n = np.array(range(50))
# Definisanje dva stepena signala
x1 = osnova1 ** n
x2 = osnova2 ** n
# Crtanje diskretnih signala
plt.stem(n, x1)
plt.title('Diskretna stepena funkcija, osnova < 1')
plt.show()
plt.stem(n, x2)
plt.title('Diskretna stepena funkcija, osnova > 1')
plt.show()

""" Prikaz diskretne polinomijalne funkcije """
# Diskretno vreme
n = np.array(range(50))
# Definisanje polinomijalnog signala
x = 5 * (n ** 2) - 3 * n + 7
# Crtanje signala
plt.stem(n, x)
plt.title('Polinomijalna funkcija')
plt.show()

""" Prikaz diskretnog polinomijalno - stepeno - trigonometrijskog signala """
# Diskretno vreme
n = np.array(range(141))
# Definisanje polinomijalno - stepeno - trigonometrijskog signala
x = (-3 * (n ** 3) + 10 * (n ** 2) - 7 * n + 15) * (0.9 ** n) * np.cos(2 * np.pi * 0.01 * n)
# Crtanje signala
plt.stem(n, x)
plt.title('Polinomijalno - stepeno - trigonometrijska funkcija')
plt.show()

""" Prikaz proizvoljnog diskretnog signala """
x = [1, 2, -2, 0, 4, 5, 7, 2, -1, 5, -3, -8, 2, 0, 5]
x = np.array(x)
n = range(x.shape[0])
# Crtanje signala
plt.stem(n, x)
plt.title('Signal x[n]')
# Imenovanje x i y - ose
plt.xlabel('diskretno vreme - n')
plt.ylabel('x[n]')

""" Šum u diskretnim signalima """
# Funkcija koja generise aditivni sum odredjenogh SNR-a i dodaje ga na prosledjeni signal
def awgn(x, target_snr_db):
    
    x_watts = x ** 2 # snaga signala
    sig_avg_watts = np.mean(x_watts) # Srednja vrednost snage
    sig_avg_db = 10 * np.log10(sig_avg_watts) # Srednja vrednost izrazena u db
    noise_avg_db = sig_avg_db - target_snr_db # Srednja vrednost snage suma u db
    noise_avg_watts = 10 ** (noise_avg_db / 10) # Srednja vrednost snage suma u vatima
    mean_noise = 0 # Srednja vrednsot Gausove raspodele
    # Sum se dobija na osnovu Gausove raspodele srednje vrednosti nula
    # i standardne devijacije koja odgovara korenu srednje vrednositi snage suma u vatima
    noise = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(x_watts))
    # dodavanje suma na prosledjeni signal
    x_noise = x + noise
    
    return x_noise

# Parametri signala
A = 50
f0 = 50
ugao = np.pi / 4
# Frekvencija odabiranja
fs = 8000
# Diskretno vreme
n = np.array(range(200))
x = A * np.cos(2 * np.pi * (fo / fs) * n + ugao)
# Zeljeni odnos signala i suma
target_snr_db = 20
# Proracun zasumljenog signala
x_noise = awgn(x, target_snr_db)
# Crtanje signala bez suma
plt.stem(range(x.shape[0]), x)
plt.title('Diskretni porstoperiodicni signal bez suma')
plt.show()
# Crtanje signala sa sumom
plt.stem(range(x.shape[0]), x_noise)
plt.title('Diskretni porstoperiodicni signal sa sumom')
plt.show()

