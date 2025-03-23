from gtts import gTTS
from googletrans import Translator
def text_to_speech(text, filename="output.mp3", speed=1.0):
    translator = Translator()
    translated = translator.translate(text, dest='hi')
    hindi_text = translated.text
    tts = gTTS(hindi_text, lang="hi", slow=False)
    tts.save(filename)
    return filename