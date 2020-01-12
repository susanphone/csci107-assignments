import pyaudio
import math
import struct

BPM = 200

Frequencies = {'A': 880, 'A#': 932, 'B':493, #these are the keys
            'C': 523, 'C#': 554, 'D': 587, 
            'D#': 622, 'E': 659, 'F': 698,
            'F#': 740, 'G': 784, 'G#': 830}

Possible_Notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#' 'G', 'G#'] 

type (Frequencies) #classified as dictionary
#word is the key
#definition is the value

