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
        # Common English to Kannada translations - Expanded Dictionary
        translation_dict = {
            # Greetings
            "hello": "ನಮಸ್ಕಾರ",
            "hi": "ಹೆಲೋ",
            "good morning": "ಶುಭೋದಯ",
            "good afternoon": "ಶುಭ ಮಧ್ಯಾಹ್ನ",
            "good evening": "ಶುಭ ಸಂಜೆ",
            "good night": "ಶುಭ ರಾತ್ರಿ",
            "goodbye": "ವಿದಾಯ",
            "bye": "ಬೈ",
            
            # Common phrases
            "thank you": "ಧನ್ಯವಾದ",
            "thanks": "ಧನ್ಯವಾದ",
            "please": "ದಯವಿಟ್ಟು",
            "sorry": "ಕ್ಷಮಿಸಿ",
            "excuse me": "ಕ್ಷಮಿಸಿ",
            "yes": "ಹೌದು",
            "no": "ಇಲ್ಲ",
            "ok": "ಠಿಕ್ಕೆ",
            "okay": "ಠಿಕ್ಕೆ",
            
            # Questions
            "how are you": "ನೀವು ಹೇಗಿದ್ದೀರಿ",
            "what is your name": "ನಿಮ್ಮ ಹೆಸರೇನು",
            "where are you from": "ನೀವು ಎಲ್ಲಿಂದ",
            "what": "ಏನು",
            "where": "ಎಲ್ಲಿ",
            "when": "ಯಾವಾಗ",
            "who": "ಯಾರು",
            "why": "ಏಕೆ",
            "how": "ಹೇಗೆ",
            
            # Personal
            "my name is": "ನನ್ನ ಹೆಸರು",
            "i am": "ನನ್ನ",
            "i love": "ನನಗೆ ಪ್ರಿಯ",
            "i like": "ನನಗೆ ಇಷ್ಟ",
            "i hate": "ನನಗೆ ದ್ವೇಷ",
            "nice to meet you": "ನಿನ್ನನ್ನು ಭೇಟಿ ಮಾಡಿ ಸಂತೋಷ",
            
            # Common objects
            "water": "ನೀರು",
            "food": "ಭೋಜನ",
            "help": "ಸಹಾಯ",
            "love": "ಪ್ರೀತಿ",
            "friend": "ಸ್ನೇಹಿ",
            "family": "ಕುಟುಂಬ",
            "home": "ಮನೆ",
            "school": "ಶಾಲೆ",
            "work": "ಕೆಲಸ",
            "book": "ಪುಸ್ತಕ",
            "money": "ಹಣ",
            "time": "ಸಮಯ",
            "day": "ದಿನ",
            "night": "ರಾತ್ರಿ",
            "year": "ವರ್ಷ",
            "hand": "ಕೈ",
            "head": "ತಲೆ",
            "eye": "ಕಣ್ಣು",
            "ear": "ಕಿವಿ",
            "mouth": "ಬಾಯಿ",
            "heart": "ಹೃದಯ",
            "leg": "ಕಾಲು",
            "foot": "ಪಾದ",
            
            # Numbers
            "one": "ಒಂದು",
            "two": "ಎರಡು",
            "three": "ಮೂರು",
            "four": "ನಾಲ್ಕು",
            "five": "ಐದು",
            "six": "ಆರು",
            "seven": "ಏಳು",
            "eight": "ಎಂಟು",
            "nine": "ಒಂಬತ್ತು",
            "ten": "ಹತ್ತು",
            
            # Adjectives
            "good": "ಒಳ್ಳೆಯ",
            "bad": "ಕೆಟ್ಟ",
            "big": "ದೊಡ್ಡ",
            "small": "ಚಿಕ್ಕ",
            "hot": "ಬಿಸಿ",
            "cold": "ಶೀತಲ",
            "happy": "ಸುಖ",
            "sad": "ದುಃಖ",
            "beautiful": "ಸುಂದರ",
            "clean": "ಸ್ವಚ್ಛ",
            "dirty": "ಕೊಳಕು",
            "strong": "ಬಲಿಷ್ಠ",
            "weak": "ದುರ್ಬಲ",
            "fast": "ವೇಗ",
            "slow": "ನಿಧಾನ",
            
            # Verbs
            "go": "ಹೋಗು",
            "come": "ಬರು",
            "run": "ಓಡು",
            "walk": "ನಡೆ",
            "sit": "ಕುಳಿತುಕೊ",
            "stand": "ನಿಂತುಕೊ",
            "eat": "ತಿನ್ನು",
            "drink": "ಕುಡಿ",
            "sleep": "ನಿದ್ರೆ",
            "wake": "ಏಳೇ",
            "play": "ಆಟ",
            "study": "ಅಧ್ಯಯನ",
            "read": "ಓದು",
            "write": "ಬರೆ",
            "speak": "ಮಾತನಾಡು",
            "listen": "ಕೆಳಗೆ",
            "see": "ನೋಡು",
            "hear": "ಕೇಳು",
            "think": "ಯೋಚಿಸು",
            "know": "ತಿಳಿ",
            "give": "ಕೊಡು",
            "take": "ತೆಗೆ",
            "make": "ಮಾಡು",
            "like": "ಇಷ್ಟ",
            "love": "ಪ್ರೀತಿ",
            
            # Places
            "india": "ಭಾರತ",
            "bangalore": "ಬೆಂಗಳೂರು",
            "kannada": "ಕನ್ನಡ",
            "english": "ಇಂಗ್ಲೀಷ",
        }
        
        # Convert to lowercase for matching
        lower_text = text.lower().strip()
        
        # Check for exact match
        if lower_text in translation_dict:
            return translation_dict[lower_text]
        
        # Sort by length (longest first) to match longer phrases first
        sorted_dict = sorted(translation_dict.items(), key=lambda x: len(x[0]), reverse=True)
        
        # Replace phrases in the text
        result = lower_text
        for english_phrase, kannada_phrase in sorted_dict:
            # Only replace if it's a whole word or phrase
            if english_phrase in result:
                # Use word boundaries for single words
                if ' ' not in english_phrase:
                    import re
                    pattern = r'\b' + re.escape(english_phrase) + r'\b'
                    result = re.sub(pattern, kannada_phrase, result, flags=re.IGNORECASE)
                else:
                    result = result.replace(english_phrase, kannada_phrase)
        
        # If no match found, return original text
        return result if result != lower_text else text


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
