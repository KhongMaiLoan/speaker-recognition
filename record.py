import nltk
#nltk.download('punkt')
import nltk.data
import pyaudio
import wave
import sys
from pynput import keyboard
import sounddevice as sd
import soundfile as sf
import time
import os



username = "abc"
filename = 'trainingData/'
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

print("Press s to start record, q to quit record, esc to exit program")


all = []


def on_press(key):
    global index
    
    if key == keyboard.Key.esc:
        stream.close()
        p.terminate()
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k in ['s']:
        print('Key pressed: ' + k)
        data = stream.read(chunk) # Record data
        all.append(data)

    if k in ['q']:
        print('Key pressed: ' + k)
        
        data = b''.join(all)
        filewavname = filename+"/"+str(username) + '.wav'
        wf = wave.open(filewavname, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

f.close()
descriptionfile.close()

