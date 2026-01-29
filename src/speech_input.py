"""
Speech-to-Text Module
Handles audio input and speech recognition
"""

import speech_recognition as sr
import os

class SpeechInput:
    """Class for handling speech input and recognition"""
    
    def __init__(self):
        """Initialize the speech recognizer"""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
    
    def record_from_microphone(self, duration=None, language='en-US'):
        """
        Record and recognize speech from microphone
        
        Args:
            duration (int): Maximum duration to record in seconds (None for no limit)
            language (str): Language code for recognition (default: 'en-US')
            
        Returns:
            str: Recognized text, or empty string if recognition failed
        """
        try:
            with self.microphone as source:
                # Adjust for ambient noise
                print("Adjusting for ambient noise... Please wait.")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                if duration:
                    print(f"Recording for {duration} seconds... Speak now!")
                    audio = self.recognizer.listen(source, timeout=duration + 2, phrase_time_limit=duration)
                else:
                    print("Recording... Speak now! (Press Ctrl+C to stop)")
                    audio = self.recognizer.listen(source, timeout=10)
                
                # Recognize speech using Google Speech Recognition
                print("Recognizing speech...")
                text = self.recognizer.recognize_google(audio, language=language)
                print(f"Recognized: {text}")
                return text
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return ""
    
    def record_from_file(self, audio_file, language='en-US'):
        """
        Recognize speech from an audio file
        
        Args:
            audio_file (str): Path to audio file
            language (str): Language code for recognition (default: 'en-US')
            
        Returns:
            str: Recognized text, or empty string if recognition failed
        """
        try:
            if not os.path.exists(audio_file):
                print(f"Audio file not found: {audio_file}")
                return ""
            
            with sr.AudioFile(audio_file) as source:
                audio = self.recognizer.record(source)
                
                print("Recognizing speech...")
                text = self.recognizer.recognize_google(audio, language=language)
                print(f"Recognized: {text}")
                return text
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return ""


if __name__ == "__main__":
    # Example usage
    speech_input = SpeechInput()
    
    # Record from microphone
    print("=== Record from Microphone ===")
    recognized_text = speech_input.record_from_microphone(duration=5)
    print(f"Result: {recognized_text}\n")
