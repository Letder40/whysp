#!/usr/bin/python3
import pytube
import sys
from os import remove

try:
    link = sys.argv[1]
except: 
    sys.stderr.write(" [!] A link must be passed as positional argument\n")
    sys.exit(1)

import whisper

try:
    model =  whisper.load_model(sys.argv[2])
except: 
    model = whisper.load_model("base")

try:
    video = pytube.YouTube(link)
except:
    sys.stderr.write(" [!] The video does not exists or it is not posible to download it\n")
    sys.exit(1)

video = video.streams.get_audio_only()
video.download(filename=".toRead.mp4")
print(" [?] video download complete, Transcribing it...")

result = model.transcribe(".toRead.mp4")
remove(".toRead.mp4")

open("transcription.txt", x).write(result["text"])
print("\n [+] Transcripttion complete ")
