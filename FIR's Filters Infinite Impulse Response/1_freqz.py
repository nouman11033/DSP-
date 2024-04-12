from scipy import signal
from matplotlib import pyplot as plt
import numpy as np


b = signal.firwin(80,0.5, window=('kaiser',8))
w,h =signal.freqz(b)

plt.semilogy(w,np.abs(h),'g')
plt.ylabel('Amplitude (db)',color='b')
plt.xlabel('Freuency (rad/sample)')

plt.show()
