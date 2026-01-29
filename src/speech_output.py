"""
Text-to-Speech Module
Handles audio output and speech synthesis
"""

from gtts import gTTS
import os
import pyttsx3
from pathlib import Path

class SpeechOutput:
    """Class for handling text-to-speech synthesis"""
    
    def __init__(self, method='google'):
        """
        Initialize the speech output handler
        
        Args:
            method (str): Method to use - 'google' (requires internet) or 'local' (offline)
        """
        self.method = method
        
        if method == 'local':
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 150)  # Speed of speech
                self.engine.setProperty('volume', 1)   # Volume level (0-1)
            except Exception as e:
                print(f"Warning: Could not initialize local TTS engine: {e}")
                self.method = 'google'
    
    def speak(self, text, language='kn'):
        """
        Speak the given text
        
        Args:
            text (str): Text to speak
            language (str): Language code (default: 'kn' for Kannada, 'en' for English)
        """
        if not text:
            return
        
        try:
            if self.method == 'google':
                self._speak_google(text, language)
            else:
                self._speak_local(text)
        except Exception as e:
            print(f"Error during speech synthesis: {e}")
    
    def _speak_google(self, text, language='kn'):
        """
        Speak using Google Text-to-Speech (requires internet)
        
        Args:
            text (str): Text to speak
            language (str): Language code
        """
        try:
            print(f"Speaking in {language}...")
            tts = gTTS(text=text, lang=language, slow=False)
            
            # Create output directory if it doesn't exist
            output_dir = Path("audio_output")
            output_dir.mkdir(exist_ok=True)
            
            # Save and play
            audio_file = output_dir / "temp_speech.mp3"
            tts.save(str(audio_file))
            
            # Play the audio
            os.system(f'start {audio_file}' if os.name == 'nt' else f'open {audio_file}')
            print(f"Playing audio: {text}")
        
        except Exception as e:
            print(f"Google TTS error: {e}")
    
    def _speak_local(self, text):
        """
        Speak using local text-to-speech engine (offline)
        
        Args:
            text (str): Text to speak
        """
        try:
            print(f"Speaking (local)...")
            self.engine.say(text)
            self.engine.runAndWait()
            print(f"Finished speaking: {text}")
        
        except Exception as e:
            print(f"Local TTS error: {e}")
    
    def save_to_file(self, text, output_file, language='kn'):
        """
        Save speech to an audio file
        
        Args:
            text (str): Text to convert to speech
            output_file (str): Path to save the audio file
            language (str): Language code
        """
        try:
            print(f"Generating speech for: {text}")
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save(output_file)
            print(f"Speech saved to: {output_file}")
            return output_file
        
        except Exception as e:
            print(f"Error saving to file: {e}")
            return None
    
    def speak_and_save(self, text, language='kn'):
        """
        Generate and save speech to a temporary file
        
        Args:
            text (str): Text to convert to speech
            language (str): Language code
            
        Returns:
            str: Path to the saved audio file, or None if failed
        """
        try:
            import tempfile
            import uuid
            
            # Create a temporary file with a unique name
            temp_dir = Path("temp_audio")
            temp_dir.mkdir(exist_ok=True)
            
            # Generate unique filename
            filename = f"speech_{uuid.uuid4().hex[:8]}.mp3"
            output_file = temp_dir / filename
            
            return self.save_to_file(text, str(output_file), language)
        
        except Exception as e:
            print(f"Error in speak_and_save: {e}")
            return None


if __name__ == "__main__":
    # Example usage
    speech_output = SpeechOutput(method='google')
    
    # Speak in Kannada
    print("=== Speak in Kannada ===")
    speech_output.speak("ನಮಸ್ಕಾರ", language='kn')
    print()
    
    # Speak in English
    print("=== Speak in English ===")
    speech_output.speak("Hello, how are you?", language='en')
