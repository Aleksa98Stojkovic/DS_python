import numpy as np
import matplotlib.pyplot as plt # biblioteka koja se koristi za crtanje grafika

# Funkcija koja formira signale i plotuje ih
def Calc_and_Plot(korak, trajanje, A, fo, ugao, scale, string):
    
    tk = np.arange(0, trajanje * korak, korak) # formiranje kontinualnog vremena sa prosledjenim korakom
    Xk = A * np.cos(2 * np.pi * fo * tk + ugao) # Proracun kontinualnog prostoperiodicnog signala 
    fs = scale * fo # odredjivanje frekvencije odabiranja
    Ts = 1 / fs # Perioda odabiranja
    td = np.arange(0, trajanje * korak, Ts) # diskretno vreme sa korakom Ts
    Xd = A * np.cos(2 * np.pi * fo * td + ugao) # Proracun diskretnog prostoperiodicnog signala
    plt.plot(tk, Xk, color = 'blue') # Graf kontinualnog signala
    plt.title('Kontinualni signal za ' + string) # Naslov grafika, + je konkatenacija za stringove
    plt.show() # Prikaz grafika 
    # --------
    # Ako izmedju dva plota ne koristimo plt.show() onda ce se oni prikazati na istoj povrsini
    # Ovde cemo na kontinualnom signalu obeleziti diskretni signal sa scatter plotom
    plt.plot(tk, Xk, color = 'blue') 
    plt.scatter(td, Xd, marker = 'x', color = 'red')
    # --------
    plt.title('Diskretni signal za ' + string)
    plt.show()
    
# Parametri prostoperiodicnog signala
A = 50 # Amplituda
ugao = 0 #Fazni stav
fo = 500 # Ucestanost

# Korak koji ce se koristiti za formiranje kontinualnog veremena
korak = 0.0001 

scale = 35 # koeficijent koji se koristi za odredjivanje vremena odabiranja
trajanje = 50 # trajanje prvog signala ce biti 5 ms
Calc_and_Plot(korak, trajanje, A, fo, ugao, scale, 'prvi slucaj')

scale = 2.23
trajanje = 200 # trajanje drugog signala ce biti 20 ms
Calc_and_Plot(korak, trajanje, A, fo, ugao, scale, 'drugi slucaj')

scale = 1.05
trajanje = 800 # trajanje prvog signala ce biti 80 ms
Calc_and_Plot(korak, trajanje, A, fo, ugao, scale, 'treci slucaj')

