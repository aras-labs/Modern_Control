import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')
print(f"sampling rate: {sampling_rate}hz") # frequency (sample per second)
print('data type:', data.dtype)
print('data shape:', data.shape)
# TODO: Calculate length of the signal in seconds
# print(f"length = {length}s")
N, no_channels = data.shape # signal length and no. of channels
print('signal length:', N)
channel0 = data[:,0]
channel1 = data[:,1]
scale = np.linspace(-2,4,N)
plt.plot(np.arange(N), scale)
plt.show()
print('shape_old:', scale.shape)
scale.shape = (N,1)
print('shape_new:', scale.shape)
data_new = data[::-1]
data_new1 = np.int16(scale * data)
scipy.io.wavfile.write('reverse.wav', sampling_rate , data_new)
scipy.io.wavfile.write('scale.wav', sampling_rate , data_new1)
scipy.io.wavfile.write('fast.wav', sampling_rate * 2 , data_new1)
scipy.io.wavfile.write('slow.wav', sampling_rate // 2 , data_new1)