from gtts import gTTS
from pydub import AudioSegment
import os

# The lib directories, which shall be TTSed
lib_en = "text/en/"
lib_de = "text/de/"

files_en = [os.path.splitext(f)[0] for f in os.listdir(lib_en) if os.path.isfile(os.path.join(lib_en, f))]
files_de = [os.path.splitext(f)[0] for f in os.listdir(lib_de) if os.path.isfile(os.path.join(lib_de, f))]

def tts(input, output, langs):
    with open(input, "r", encoding="utf-8") as file:
        text = file.read()
    tts = gTTS(text, lang=langs)
    tts.save(output + ".wav")

def convertWavToMp3(path, to):
    sound = AudioSegment.from_wav(path + ".wav")
    sound.export(to + ".mp3", format="mp3", bitrate="192k")

def main():
    for file in files_en:
        tts(lib_en + file + ".txt", "audio/wav/en/" + file, "en")
    for file in files_de:
        tts(lib_de + file + ".txt", "audio/wav/de/" + file, "de")
    # Conversion does not work on me
    # for file in files_en:
    #     convertWavToMp3("audio/wav/en/" + file, "audio/mp3/en/" + file)
    # for file in files_de:
    #     convertWavToMp3("audio/wav/de/" + file, "audio/mp3/de/" + file)

if __name__ == "__main__":
    main()
