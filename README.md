Script that includes a python script that turns text files into wav files using the Google TTS API and also a script to delete the generated audio.

First of all besides Python, which you to have installed, you need to run:

    pip install gtts
    pip install pydub
    pip install ffmpeg

Directory management:

    audio (here your generated audio files will be stored)
      mp3
        de
        en
      wav
        de
        en
    text (here your given text files need to be stored) 
      de
      en
    delete_audio.py
    tts.py
