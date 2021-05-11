import sounddevice
from scipy.io.wavfile import write
import wave
import numpy as np
import sys
#import matplotlib.pyplot as plt
duration=10
fs=44100

#rec steht für record
print("aufnahme läuft")
aufnahme_1=sounddevice.rec(int(duration * fs),samplerate=fs,channels=1)
sounddevice.wait()
write("output2_ch2.wav",fs,aufnahme_1)

"""For subploting the form""
wav=wave.open("output1_ch1.wav","r")
raw = wav.readframes(-1)
raw=np.frombuffer(raw,"Int16")
sampleRate = wav.getframerate()

if wav.getchannels== 2:
    print("Audio is stereo i only need mono")
    sys.exit(0)

Time=np.linspace(0,len(raw)/sampleRate,num=len(raw))
plt.title("Subploting the form of the Mono signal")
plt.plot(Time,raw,color="blue")
plt.ylabel("Amplitude")
plt.show() """

"""Optimization"""


#time.sleep(duration)
#
"""speicherbedarf
Samplerate
kanal"""