from translate import Translator

def translate(text, source_language, dest_language):
    translator = Translator(from_lang=source_language, to_lang=dest_language)
    translated_text = translator.translate(text)
    return translated_text