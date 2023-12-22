Script that includes a python script that turns text files into wav files using the Google TTS API and also a script to delete the generated audio.

First of all besides Python, which you need to have installed, you need to run:

    pip install gtts
    pip install pydub
and

    pip install ffmpeg
(does not really work sadly)

Directory management:

    audio (your generated audio files will be stored here)
      mp3
      wav
    text (your given text files need to be stored here) 
      de
      en
      ru
    delete_audio.py
    tts.py
