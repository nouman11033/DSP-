from scipy.signal import freqz, remez
from matplotlib import pyplot as plt
import numpy as np

#Filter with passband 0.2-0.4hz, stopband 0-0.1Hz and 0.45-0.5Hz

bpass = remez(72,[0,0.1,0.2,0.4,0.45,0.5],[0,1,0])
freq, response = freqz(bpass)
amp = abs(response)

plt.semilogy(freq/(2*np.pi),amp,'g-')
plt.grid()
plt.show()
   
