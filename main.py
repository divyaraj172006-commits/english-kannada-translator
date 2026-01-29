"""
Main Application
English to Kannada Translator with Text and Speech Support
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from translator import EnglishKannadaTranslator
from speech_input import SpeechInput
from speech_output import SpeechOutput


class TranslatorApp:
    """Main application class for the translator"""
    
    def __init__(self):
        """Initialize the application"""
        self.translator = EnglishKannadaTranslator()
        self.speech_input = SpeechInput()
        self.speech_output = SpeechOutput(method='google')  # or 'local'
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("English to Kannada Translator")
        print("="*50)
        print("1. Translate Text")
        print("2. Translate from Speech (Voice Input)")
        print("3. Translate Text with Speech Output")
        print("4. Full Translation (Speech to Text)")
        print("5. Exit")
        print("="*50)
    
    def translate_text_menu(self):
        """Handle text translation"""
        print("\n--- Text Translation ---")
        english_text = input("Enter English text to translate: ").strip()
        
        if not english_text:
            print("No text provided!")
            return
        
        kannada_text = self.translator.translate_text(english_text)
        print(f"\nEnglish: {english_text}")
        print(f"Kannada: {kannada_text}")
        
        # Ask if user wants to hear the translation
        speak = input("\nWould you like to hear the translation? (yes/no): ").strip().lower()
        if speak in ['yes', 'y']:
            self.speech_output.speak(kannada_text, language='kn')
    
    def translate_from_speech_menu(self):
        """Handle speech to text translation"""
        print("\n--- Voice Input Translation ---")
        print("Please speak in English...")
        
        english_text = self.speech_input.record_from_microphone(duration=5, language='en-US')
        
        if not english_text:
            print("Could not recognize speech!")
            return
        
        kannada_text = self.translator.translate_text(english_text)
        print(f"\nEnglish: {english_text}")
        print(f"Kannada: {kannada_text}")
        
        # Ask if user wants to hear the translation
        speak = input("\nWould you like to hear the translation? (yes/no): ").strip().lower()
        if speak in ['yes', 'y']:
            self.speech_output.speak(kannada_text, language='kn')
    
    def translate_with_speech_output_menu(self):
        """Handle text translation with speech output"""
        print("\n--- Text Translation with Voice Output ---")
        english_text = input("Enter English text to translate: ").strip()
        
        if not english_text:
            print("No text provided!")
            return
        
        kannada_text = self.translator.translate_text(english_text)
        print(f"\nEnglish: {english_text}")
        print(f"Kannada: {kannada_text}")
        print("\nPlaying Kannada translation...")
        self.speech_output.speak(kannada_text, language='kn')
    
    def full_translation_menu(self):
        """Handle full translation: speech input to speech output"""
        print("\n--- Full Translation (Voice Input & Output) ---")
        print("Please speak in English...")
        
        english_text = self.speech_input.record_from_microphone(duration=5, language='en-US')
        
        if not english_text:
            print("Could not recognize speech!")
            return
        
        kannada_text = self.translator.translate_text(english_text)
        print(f"\nEnglish: {english_text}")
        print(f"Kannada: {kannada_text}")
        print("\nPlaying Kannada translation...")
        self.speech_output.speak(kannada_text, language='kn')
    
    def run(self):
        """Run the main application loop"""
        print("\n" + "="*50)
        print("Welcome to English-Kannada Translator!")
        print("="*50)
        
        while True:
            self.display_menu()
            choice = input("Select an option (1-5): ").strip()
            
            if choice == '1':
                self.translate_text_menu()
            elif choice == '2':
                self.translate_from_speech_menu()
            elif choice == '3':
                self.translate_with_speech_output_menu()
            elif choice == '4':
                self.full_translation_menu()
            elif choice == '5':
                print("\nThank you for using the translator!")
                print("Goodbye!")
                break
            else:
                print("Invalid option! Please select 1-5.")


if __name__ == "__main__":
    app = TranslatorApp()
    app.run()
