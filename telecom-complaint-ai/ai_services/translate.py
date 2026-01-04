from googletrans import Translator
from langdetect import detect

translator = Translator()

def translate_to_english(text):
    try:
        detected_lang = detect(text)

        # Force Telugu / Hindi / others to English
        if detected_lang != "en":
            translated = translator.translate(text, dest="en")
            return translated.text, detected_lang

        return text, "en"

    except:
        # If detection fails, still try translation
        translated = translator.translate(text, dest="en")
        return translated.text, "unknown"
