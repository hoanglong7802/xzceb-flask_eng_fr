"""
translator.py: A module for English to French and French to English translation.
"""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """
    Translates English text to French.
    Args:
        english_text (str): The English text to be translated.
    Returns:
        str: The translated text in French.
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def frenchToEnglish(french_text):
    """
    Translates French text to English.
    Args:
        frenchText (str): The French text to be translated.
    Returns:
        str: The translated text in English.
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
