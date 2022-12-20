# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 03:25:41 2022

@author: Matthew
"""

import json
import pyaudio
from vosk import Model, KaldiRecognizer

class Listen:
    
    model = Model(r'H:\Assistant\Assistant\Model\vosk-model-en-us-0.42-gigaspeech')

    rec = KaldiRecognizer(model, 16000)


    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    stream.start_stream()

    # listing loop 
    while True:
    
        data = stream.read(4096, exception_on_overflow=False)
        
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)
            text = result['text']
            print(text)
            
        if text == 'stop':
           break
    
    
listen = Listen()