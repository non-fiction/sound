# -*- coding: utf-8 -*-

import wave
import numpy as np
from matplotlib import pylab as plt
import struct

a = 1     #�U��
fs = 8000 #�T���v�����O���g��
f0 = 440  #���g��
sec = 5   #�b

swav=[]

for n in np.arange(fs * sec):
    #�T�C���g�𐶐�
    s = a * np.sin(2.0 * np.pi * f0 * n / fs)
    swav.append(s)

#�T�C���g��\��
plt.plot(swav[0:100])
plt.show()

#�T�C���g��-32768����32767�̐����l�ɕϊ�(signed 16bit pcm��)
swav = [int(x * 32767.0) for x in swav]

#�o�C�i����
binwave = struct.pack("h" * len(swav), *swav)

#�T�C���g��wav�t�@�C���Ƃ��ď����o��
w = wave.Wave_write("d:\work\output.wav")
p = (1, 2, 8000, len(binwave), 'NONE', 'not compressed')
w.setparams(p)
w.writeframes(binwave)
w.close()


