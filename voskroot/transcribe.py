#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import json

SetLogLevel(0)

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

sample_rate=16000
model = Model("model")
rec = KaldiRecognizer(model, sample_rate)

process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            sys.argv[1],
                            '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                            stdout=subprocess.PIPE)

filename1 = sys.argv[1]
filename1 = filename1.replace('audio','text')
sys.stdout = open(filename1+'.txt', 'x')

while True:
    data = process.stdout.read(4000)
    #with open("myfile.txt", "w") as file1:
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        print (res['text'])
        #with open("myfile.txt", "w") as file1:
        # Writing data to a file
        #file1.write(res['text'])
    

res = json.loads(rec.FinalResult())
print (res['text'])
#file1.write(res['text'])
#file1.close()
