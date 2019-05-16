# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:07:35 2019

@author: Desktop-TL
"""
from midiutil import MIDIFile
from itertools import cycle
import pandas as pd

# %% Notes
A = 57
Asharp = 58
B = 59
C = 60
Csharp = 61
D = 62
Dsharp = 63
E = 64
F = 65
Fsharp = 66
G = 67
Gsharp = 68

# %% Keys
Chromatic = [A, Asharp, B, C, Csharp, D, Dsharp, E, F, Fsharp, G, Gsharp]
MajorKeys = pd.DataFrame()
MinorKeys = pd.DataFrame()
MajorScale = [0, 2, 4, 5, 7, 9, 11, 12]
MinorScale = [0, 2, 3, 5, 7, 8, 10, 12]

names = ['A', 'Asharp', 'B', 'C', 'Csharp', 'D',
         'Dsharp', 'E', 'F', 'Fsharp', 'G', 'Gsharp']

for ix, root in enumerate(Chromatic):
    tmp_keys = []
    for num in MajorScale:
        tmp_num = root+num
        tmp_keys.append(tmp_num)
    MajorKeys[names[ix]] = tmp_keys

for ix, root in enumerate(Chromatic):
    tmp_keys = []
    for num in MinorScale:
        tmp_num = root+num
        tmp_keys.append(tmp_num)
    MinorKeys[names[ix]] = tmp_keys
    
# %% Chord Progressions
Chord1 = [MajorKeys['Csharp'], MajorKeys['Gsharp'], MinorKeys['Asharp'], MinorKeys['F']]

# %% Making the MIDI file
track = 0
time = 0    # in Beats
tempo = 100  # in BPM

channel = [0, 2, 4]
duration = 4
volume = 100

loopnumber = 10

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track, time, tempo)

for num in range(loopnumber):
    for chordnumber in Chord1:
        degrees = chordnumber.values
        for n_channel in channel:
            MyMIDI.addNote(track, n_channel, degrees[n_channel], time, duration, volume)
        time = time + 4

with open("test_scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

for num in range(len(Chord1)):
    print(Chord1[num].name)   
    