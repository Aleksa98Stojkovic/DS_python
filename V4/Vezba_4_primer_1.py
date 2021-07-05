import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import blackman, hamming, hann, kaiser, triang, boxcar
from scipy.signal import firwin

""" Primer za NF filtar """

# Specifikacija NF filtra
Wn = 0.3 # jer je kriticna ucestanost zadata kao 2 * pi * 0.15 = 0.3 * pi
N = 24
# projektovanje FIR filtara koristeci razlicite prozorske funkcije
b1 = firwin(N, Wn, window = 'boxcar', pass_zero = 'lowpass')
b2 = firwin(N, Wn, window = 'hann', pass_zero = 'lowpass')
b3 = firwin(N, Wn, window = 'hamming', pass_zero = 'lowpass')
b4 = firwin(N, Wn, window = 'blackman', pass_zero = 'lowpass')
# Racunanje spektra u 1024 tacke
N_fft = 1024
B1 = fft(b1, N_fft)
B2 = fft(b2, N_fft)
B3 = fft(b3, N_fft)
B4 = fft(b4, N_fft)
# Amplitudske karakteristike 
B1a = np.abs(B1[: N_fft // 2])
B2a = np.abs(B2[: N_fft // 2])
B3a = np.abs(B3[: N_fft // 2])
B4a = np.abs(B4[: N_fft // 2])
# Crtanje amplitudskih karakteristika na linearnoj skali
n = np.array(range(N_fft // 2))
w = n * np.pi / (np.amax(n))
plt.subplot(2, 2, 1)
plt.plot(w, B1a)
plt.title('NF filtar - pravougaoni prozor')
plt.subplot(2, 2, 2)
plt.plot(w, B2a)
plt.title('NF filtar - Hanov prozor')
plt.subplot(2, 2, 3)
plt.plot(w, B3a)
plt.title('NF filtar - Hamingov prozor')
plt.subplot(2, 2, 4)
plt.plot(w, B4a)
plt.title('NF filtar - Blekmanov prozor')
plt.show()
# Crtanje aplitudskih karakteristika na jednom grafiku
plt.subplot(2, 1, 1)
plt.plot(w, B1a)
plt.plot(w, B2a, color = 'green')
plt.plot(w, B3a, color = 'red')
plt.plot(w, B4a, color = 'yellow')
plt.legend(['NF filtar - pravougaoni prozor', 'NF filtar - Hanov prozor',
            'NF filtar - Hamingov prozor', 'NF filtar - Blekmanov prozor'])
plt.subplot(2, 1, 2)
plt.plot(w, 20 * np.log10(B1a))
plt.plot(w, 20 * np.log10(B2a), color = 'green')
plt.plot(w, 20 * np.log10(B3a), color = 'red')
plt.plot(w, 20 * np.log10(B4a), color = 'yellow')
plt.legend(['NF filtar - pravougaoni prozor', 'NF filtar - Hanov prozor',
            'NF filtar - Hamingov prozor', 'NF filtar - Blekmanov prozor'])
plt.show()

""" Primer za PO filtar """

# Specifikacija PO filtra
Wn = [0.2, 0.6] # %jer su kriticne ucestanosti zadate kao wc1 = 0.2 * pi, wc2 = 0.6 * pi
N = 30
# projektovanje FIR filtara koristeci razlicite prozorske funkcije
b1 = firwin(N, Wn, window = 'boxcar', pass_zero = 'bandpass')
b2 = firwin(N, Wn, window = 'hann', pass_zero = 'bandpass')
b3 = firwin(N, Wn, window = 'hamming', pass_zero = 'bandpass')
b4 = firwin(N, Wn, window = 'blackman', pass_zero = 'bandpass')
# Racunanje spektra u 1024 tacke
N_fft = 1024
B1 = fft(b1, N_fft)
B2 = fft(b2, N_fft)
B3 = fft(b3, N_fft)
B4 = fft(b4, N_fft)
# Amplitudske karakteristike 
B1a = np.abs(B1[: N_fft // 2])
B2a = np.abs(B2[: N_fft // 2])
B3a = np.abs(B3[: N_fft // 2])
B4a = np.abs(B4[: N_fft // 2])
# Crtanje amplitudskih karakteristika na linearnoj skali
n = np.array(range(N_fft // 2))
w = n * np.pi / (np.amax(n))
plt.subplot(2, 2, 1)
plt.plot(w, B1a)
plt.title('NF filtar - pravougaoni prozor')
plt.subplot(2, 2, 2)
plt.plot(w, B2a)
plt.title('NF filtar - Hanov prozor')
plt.subplot(2, 2, 3)
plt.plot(w, B3a)
plt.title('NF filtar - Hamingov prozor')
plt.subplot(2, 2, 4)
plt.plot(w, B4a)
plt.title('NF filtar - Blekmanov prozor')
plt.show()
# Crtanje aplitudskih karakteristika na jednom grafiku
plt.subplot(2, 1, 1)
plt.plot(w, B1a)
plt.plot(w, B2a, color = 'green')
plt.plot(w, B3a, color = 'red')
plt.plot(w, B4a, color = 'yellow')
plt.legend(['NF filtar - pravougaoni prozor', 'NF filtar - Hanov prozor',
            'NF filtar - Hamingov prozor', 'NF filtar - Blekmanov prozor'])
plt.subplot(2, 1, 2)
plt.plot(w, 20 * np.log10(B1a))
plt.plot(w, 20 * np.log10(B2a), color = 'green')
plt.plot(w, 20 * np.log10(B3a), color = 'red')
plt.plot(w, 20 * np.log10(B4a), color = 'yellow')
plt.legend(['NF filtar - pravougaoni prozor', 'NF filtar - Hanov prozor',
            'NF filtar - Hamingov prozor', 'NF filtar - Blekmanov prozor'])
plt.show()
