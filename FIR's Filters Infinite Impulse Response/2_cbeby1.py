from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style

import numpy as np


b,a = signal.cheby1(4,5,100,'low',analog=True)
w,h = signal.freqs(b,a)

#style.use('dark_background')

plt.plot(w,20*np.log10(abs(h)))
plt.xscale('log')
plt.title("Chebyshev Type I frequency response (rp=5)")
plt.xlabel("Frequency (rad/second)")
plt.ylabel("Amplitude (dB)")
plt.margins(0,0.1)
plt.grid(which='both', axis='both')
plt.axvline(100,color='green')
plt.axhline(-5,color='green')
plt.show()
