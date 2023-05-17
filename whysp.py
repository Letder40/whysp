import pytube
import whisper
import sys
from os import remove

#### PROVISIONAL CODE FOR NUMBA DEPRECATION WARNING
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
#### ----------------------------------------------

model = whisper.load_model("small")

try:
    link = sys.argv[1]
except: 
    sys.stderr.write("A link must be passed as positional argument\n")
    sys.exit(1)

try:
    video = pytube.YouTube(link)
except:
    sys.stderr.write("The video does not exists or it is not posible to download it\n")
    sys.exit(1)

video = video.streams.get_audio_only()
video.download(filename=".toRead.mp4")


result = model.transcribe(".toRead.mp4")
remove(".toRead.mp4")
print(result["text"])