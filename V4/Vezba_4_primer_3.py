import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import blackman, hamming, hann, kaiser, triang, boxcar
from scipy.signal import firwin

pi = np.pi

# Specifikacija NO filtra 
wp1 = 0.2 * pi
wp2 = 0.75 * pi 
ws1 = 0.25 * pi 
ws2 = 0.7 * pi
Ap = 1
As = 30
 
# korak 1: odredjivanje dw, wc, delta_s i delta_p 
dw = min(ws1 - wp1, wp2 - ws2)
wc1 = wp1 + dw / 2 
wc2 = wp2 - dw / 2 
delta_s = 10 ** (-0.05 * As) 
delta_p = (10 ** (0.05 * Ap) - 1) / (10 ** (0.05 * Ap) + 1) 

# korak 2: odredjivanje delta 
delta = min(delta_s, delta_p) 
if delta is not delta_s: 
    delta_s = -20 * np.log10(delta) 
 
# korak 3: odredjivanje beta 
beta = 0
if As >= 21 and As <= 50: 
    beta = 0.5842 * (As - 21) ** 0.4 + 0.07886 * (As - 21)

if As > 50:
    beta = 0.1102 * (As - 8.7) 

# korak 4: odredjivanje M 
D = 0.9222 
if As > 21: 
    D = (As - 7.95) / 14.36 

M = np.ceil(2 * pi * D / dw + 1) 
# ukoliko je M paran dodaj jedan da bi smo dobili neparan broj 
# ovo je neophodno da bi projektovani filtar imao celobrojno kasnjenje 
if M % 2 == 0: 
    M = M + 1
    
# korak 5: projektovanje FIR filtra 
N = int(M) # potrebni red filtra 
Wn = [wc1 / pi, wc2 / pi] # specifikacija nepropusnog opsega 
b = firwin(N, Wn, window = ('kaiser', beta), pass_zero = 'bandstop') 
# racunanje spektra u 1024 tacke koriscenjem FFT 
N_fft = 1024 
B = fft(b, N_fft) 
# odredjivanje amplitudske karakteristike 
Ba = np.abs(B[: N_fft // 2]) 
# crtanje amplitudskih karakteristika na jednom grafiku 
n = np.array(range(N_fft // 2)) 
w = n * pi / (np.amax(n)) 
plt.subplot(2, 1, 1)
plt.plot(w, Ba)
plt.title('Amplitudska karakteristika NO filtra projektovanog koriscenjem Kajzerovog prozora - linearna osa') 
plt.subplot(2, 1, 2)
plt.plot(w, 20 * np.log10(Ba))
plt.title('Amplitudska karakteristika NO filtra projektovanog koriscenjem Kajzerovog prozora - logaritamska osa')