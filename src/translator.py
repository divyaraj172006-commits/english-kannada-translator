"""
English to Kannada Translator Module
This module provides text translation capabilities from English to Kannada
"""

from google.cloud import translate_v2
import os

class EnglishKannadaTranslator:
    """Translator class for English to Kannada translation"""
    
    def __init__(self, credentials_path=None):
        """
        Initialize the translator
        
        Args:
            credentials_path (str): Path to Google Cloud credentials JSON file
        """
        # Set credentials path if provided
        if credentials_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
        
        try:
            # Initialize Google Translate client
            self.translate_client = translate_v2.Client()
        except Exception as e:
            print(f"Warning: Could not initialize Google Translate: {e}")
            print("Using fallback dictionary translation method")
            self.translate_client = None
    
    def translate_text(self, text):
        """
        Translate English text to Kannada
        
        Args:
            text (str): English text to translate
            
        Returns:
            str: Translated Kannada text
        """
        if not text:
            return ""
        
        try:
            if self.translate_client:
                # Use Google Translate API
                result = self.translate_client.translate_text(
                    source_language='en',
                    target_language='kn',
                    values=[text]
                )
                return result['translations'][0]['translatedText']
            else:
                # Fallback to simple dictionary method
                return self._fallback_translate(text)
        except Exception as e:
            print(f"Translation error: {e}")
            return text
    
    def _fallback_translate(self, text):
        """
        Fallback translation method using a dictionary
        (Limited - covers common phrases only)
        
        Args:
            text (str): English text to translate
            
        Returns:
            str: Translated Kannada text (or original if not in dictionary)
        """
        # Common English to Kannada translations
        translation_dict = {
            "hello": "ನಮಸ್ಕಾರ",
            "good morning": "ಶುಭೋದಯ",
            "good evening": "ಶುಭ ಸಂಧ್ಯೆ",
            "thank you": "ಧನ್ಯವಾದ",
            "yes": "ಹೌದು",
            "no": "ಇಲ್ಲ",
            "sorry": "ಕ್ಷಮಿಸಿ",
            "how are you": "ನೀವು ಹೇಗಿದ್ದೀರಿ",
            "what is your name": "ನಿಮ್ಮ ಹೆಸರೇನು",
            "my name is": "ನನ್ನ ಹೆಸರು",
            "water": "ನೀರು",
            "food": "ಭೋಜನ",
            "help": "ಸಹಾಯ",
            "goodbye": "ವಿದಾಯ",
        }
        
        # Convert to lowercase for matching
        lower_text = text.lower().strip()
        
        # Check for exact match
        if lower_text in translation_dict:
            return translation_dict[lower_text]
        
        # Check for partial matches
        for key, value in translation_dict.items():
            if key in lower_text:
                return text.replace(key, value, 1)
        
        # If no match found, return original text
        return text


if __name__ == "__main__":
    # Example usage
    translator = EnglishKannadaTranslator()
    
    # Test translations
    test_sentences = [
        "Hello, how are you?",
        "Thank you for your help",
        "What is your name?"
    ]
    
    for sentence in test_sentences:
        translated = translator.translate_text(sentence)
        print(f"English: {sentence}")
        print(f"Kannada: {translated}")
        print()
