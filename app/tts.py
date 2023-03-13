from gtts import gTTS
from io import BytesIO


def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()
