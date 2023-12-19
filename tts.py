from gtts import gTTS

# Your file from the lib directory here, which shall be spoken
text_file = "quandale_dingle"

lib = "./lib/"
input_path = lib + text_file + ".txt"
output_path_wav = "audio/" + text_file + ".wav"

with open(input_path, "r", encoding="utf-8") as file:
    text = file.read()

tts = gTTS(text)
tts.save(output_path_wav)