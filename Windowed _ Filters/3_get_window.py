from matplotlib import pyplot as plt
import mysignals as sigs
from scipy import signal
from matplotlib import style
import numpy as np




triang_window  = signal.get_window('triang',30)
kaiser_window  = signal.get_window(('kaiser',4.0),30)
kaiser_window2  = signal.get_window(4.0,30)
hamm_window    = signal.get_window('hamming',30)
black_window   = signal.get_window('blackman',30)




style.use('dark_background')

f, plt_arr =plt.subplots(4,sharex=True)
f.suptitle('Windows')

plt_arr[0].plot(triang_window,color='red')
plt_arr[0].set_title("Triangular Window ", color ='red')

plt_arr[1].plot(kaiser_window,color='red')
plt_arr[1].set_title(" Kaiser Window ", color ='red')

plt_arr[2].plot(hamm_window,color='red')
plt_arr[2].set_title("Hamming Window ", color ='red')

plt_arr[3].plot(black_window,color='red')
plt_arr[3].set_title(" Blackman Window", color ='red')
plt.show()
