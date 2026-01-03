from langdetect import detect
from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    try:
        lang = detect(text)
        if lang != "en":
            translated = translator.translate(text, dest="en")
            return translated.text, lang
        return text, "en"
    except:
        return text, "unknown"
