import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import boxcar, blackman, hamming, hann, kaiser, triang

# Definisanje pravougaonog prozora duzine 32 odbirka
N = 32
w = boxcar(N)
# Crtanje prozora
plt.stem(range(N), w)
plt.title('Pravougaoni prozor, N = 32')
plt.show()
# Određivanje spektralne karakteristike
W = fft(w, 1024)
# Normalizacija spektra tako da W[0] = 1, odnosno W[0] = 0 dB
Wnorm = np.abs(W) / np.abs(W[0])
# Crtanje spektralne karakteristike
plt.plot(np.pi * (np.array(range(len(W) // 2))) / 512, 20 * np.log10(Wnorm[0 : len(W) // 2]))
plt.axis([0, np.pi, -60, 0])
plt.title('Amplitudska karakteristika pravougaonog prozora u dB')
plt.show()


# Definisanje trougaonog prozora duzine 32 odbirka
N = 32
w = triang(N)
# Crtanje prozora
plt.stem(range(N), w)
plt.title('Trougaoni prozor, N = 32')
plt.show()
# Određivanje spektralne karakteristike
W = fft(w, 1024)
# Normalizacija spektra tako da W[0] = 1, odnosno W[0] = 0 dB
Wnorm = np.abs(W) / np.abs(W[0])
# Crtanje spektralne karakteristike
plt.plot(np.pi * (np.array(range(len(W) // 2))) / 512, 20 * np.log10(Wnorm[0 : len(W) // 2]))
plt.title('Amplitudska karakteristika trougaonog prozora u dB')
plt.show()


# Definisanje Hanovog prozora duzine 32 odbirka
N = 32
w = hann(N)
# Crtanje prozora
plt.stem(range(N), w)
plt.title('Hanov prozor, N = 32')
plt.show()
# Određivanje spektralne karakteristike
W = fft(w, 1024)
# Normalizacija spektra tako da W[0] = 1, odnosno W[0] = 0 dB
Wnorm = np.abs(W) / np.abs(W[0])
# Crtanje spektralne karakteristike
plt.plot(np.pi * (np.array(range(len(W) // 2))) / 512, 20 * np.log10(Wnorm[0 : len(W) // 2]))
plt.title('Amplitudska karakteristika Hanovog prozora u dB')
plt.show()


# Definisanje Hamingovog prozora duzine 32 odbirka
N = 32
w = hamming(N)
# Crtanje prozora
plt.stem(range(N), w)
plt.title('Hamingovog prozor, N = 32')
plt.show()
# Određivanje spektralne karakteristike
W = fft(w, 1024)
# Normalizacija spektra tako da W[0] = 1, odnosno W[0] = 0 dB
Wnorm = np.abs(W) / np.abs(W[0])
# Crtanje spektralne karakteristike
plt.plot(np.pi * (np.array(range(len(W) // 2))) / 512, 20 * np.log10(Wnorm[0 : len(W) // 2]))
plt.title('Amplitudska karakteristika Hamingovog prozora u dB')
plt.show()


# Definisanje Blekmanovog prozora duzine 32 odbirka
N = 32
w = blackman(N)
# Crtanje prozora
plt.stem(range(N), w)
plt.title('Blekmanov prozor, N = 32')
plt.show()
# Određivanje spektralne karakteristike
W = fft(w, 1024)
# Normalizacija spektra tako da W[0] = 1, odnosno W[0] = 0 dB
Wnorm = np.abs(W) / np.abs(W[0])
# Crtanje spektralne karakteristike
plt.plot(np.pi * (np.array(range(len(W) // 2))) / 512, 20 * np.log10(Wnorm[0 : len(W) // 2]))
plt.title('Amplitudska karakteristika Blekmanovog prozora u dB')
plt.show()


# Definisanje Kajzerovog prozora duzine 32 odbirka za tri vrednosti beta
N = 32
w1 = kaiser(N, 4) # beta = 4
w2 = kaiser(N, 7) # beta = 7
w3 = kaiser(N, 10) # beta = 10
# Crtanje prozora

plt.subplot(3, 1, 1)
plt.stem(range(N), w1)
# Grcko slovo beta se koduje sa \u03B2
plt.title('Kajzerov prozor, N = 32 i \u03B2 = 4')
plt.subplot(3, 1, 2)
plt.stem(range(N), w2)
plt.title('Kajzerov prozor, N = 32 i \u03B2 = 7')
plt.subplot(3, 1, 3)
plt.stem(range(N), w2)
plt.title('Kajzerov prozor, N = 32 i \u03B2 = 10')
plt.show()
# Određivanje spektralne karakteristike sva tri prozora
W1 = fft(w1, 1024)
W2 = fft(w2, 1024)
W3 = fft(w3, 1024)
# Normalizacija spektra tako da W[0] = 1, odnosno W[0] = 0 dB
Wnorm1 = np.abs(W1) / np.abs(W1[0])
Wnorm2 = np.abs(W2) / np.abs(W2[0])
Wnorm3 = np.abs(W3) / np.abs(W3[0])
# Crtanje spektralne karakteristike
plt.subplot(3, 1, 1)
plt.plot(np.pi * (np.array(range(len(W1) // 2))) / 512, 20 * np.log10(Wnorm1[0 : len(W1) // 2]))
plt.title('Amplitudska karakteristika Kajzerovog prozora u dB za \u03B2 = 4')
plt.subplot(3, 1, 2)
plt.plot(np.pi * (np.array(range(len(W2) // 2))) / 512, 20 * np.log10(Wnorm2[0 : len(W2) // 2]))
plt.title('Amplitudska karakteristika Kajzerovog prozora u dB za \u03B2 = 7')
plt.subplot(3, 1, 3)
plt.plot(np.pi * (np.array(range(len(W3) // 2))) / 512, 20 * np.log10(Wnorm3[0 : len(W3) // 2]))
plt.title('Amplitudska karakteristika Kajzerovog prozora u dB za \u03B2 = 10')
plt.show()