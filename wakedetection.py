# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 03:02:48 2022

@author: Matthew
"""

import pvporcupine
import struct
import pyaudio

porcupine = None
pa = None
audio_stream = None

porcupine = pvporcupine.create(access_key="7M/LimELEfEmpALzIF9uqRko6m52LpRRnE7TPYKZV20skixnD23h6Q==" , keyword_paths=["H:\Assistant\Assistant\Model\Hey-maki_en_windows_v2_1_0.ppn"])

mic = pyaudio.PyAudio()

audio_stream = mic.open(format=pyaudio.paInt16, channels=1, rate=porcupine.sample_rate, input=True, frames_per_buffer=porcupine.frame_length)

while True:
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h"* porcupine.frame_length,pcm)
    
    keyword_index = porcupine.process(pcm)
    
    if keyword_index >= 0:
        print("Hotword detected")
        
        if audio_stream is not None:
            audio_stream.close()


