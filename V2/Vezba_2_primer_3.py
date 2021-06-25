import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

b_fir = [0.4785, 0.31518, 0.019508, -0.099511, -0.018267, 0.053488, 0.016344,
        -0.032272, -0.013935, 0.019887, 0.011274, -0.011995, -0.0085958,
        0.0068719, 0.0061108, -0.0036272, -0.0039768, 0.0042645]
a_fir = [1]

b_iir = [0.4785, 0.31518, 0.019508, -0.099511, -0.018267]
a_iir = [1, -3.614, 5.0702, -3.2616, 0.81451]

n = range(100)
delta_impuls = np.zeros(len(n))
delta_impuls[0] = 1

g_fir = lfilter(b_fir, a_fir, delta_impuls)
g_iir = lfilter(b_iir, a_iir, delta_impuls)

plt.subplot(2, 1, 1)
plt.stem(n, g_fir)
plt.title('Impulsni odziv FIR sistema')
plt.subplot(2, 1, 2)
plt.stem(n, g_iir)
plt.title('Impulsni odziv IIR sistema')
plt.show()