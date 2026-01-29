#!/usr/bin/env python3
"""
Example usage and testing script for English to Kannada Translator
Run this to test all features without the web interface
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from translator import EnglishKannadaTranslator
from speech_input import SpeechInput
from speech_output import SpeechOutput


def test_text_translation():
    """Test text translation feature"""
    print("\n" + "="*60)
    print("TEST 1: Text Translation")
    print("="*60)
    
    translator = EnglishKannadaTranslator()
    
    test_phrases = [
        "Hello",
        "Good morning",
        "Thank you",
        "How are you?",
        "What is your name?",
        "I love learning Kannada",
    ]
    
    for phrase in test_phrases:
        result = translator.translate_text(phrase)
        print(f"English: {phrase:30} → Kannada: {result}")
    
    print("\n✓ Text translation test completed")


def test_speech_output():
    """Test speech output (text-to-speech)"""
    print("\n" + "="*60)
    print("TEST 2: Text-to-Speech Output")
    print("="*60)
    
    speech_output = SpeechOutput(method='google')
    
    kannada_texts = [
        "ನಮಸ್ಕಾರ",
        "ಧನ್ಯವಾದ",
        "ಹೌದು",
    ]
    
    print("These would be spoken (audio generation test):")
    for text in kannada_texts:
        print(f"  - {text}")
    
    # Try to generate audio
    try:
        audio_path = speech_output.speak_and_save("ನಮಸ್ಕಾರ", language='kn')
        if audio_path:
            print(f"✓ Audio saved to: {audio_path}")
        else:
            print("⚠ Audio generation attempted (may require internet)")
    except Exception as e:
        print(f"⚠ Audio generation test: {e}")
    
    print("\n✓ Speech output test completed")


def test_full_translation_flow():
    """Test complete translation flow"""
    print("\n" + "="*60)
    print("TEST 3: Full Translation Flow")
    print("="*60)
    
    translator = EnglishKannadaTranslator()
    
    # Simulate a complete flow
    english_text = "Good morning, how are you today?"
    print(f"1. Input English: {english_text}")
    
    kannada_text = translator.translate_text(english_text)
    print(f"2. Translated to Kannada: {kannada_text}")
    
    speech_output = SpeechOutput(method='google')
    print(f"3. Would generate speech for: {kannada_text}")
    
    print("\n✓ Full translation flow test completed")


def test_api_endpoints_simulation():
    """Simulate what the API endpoints would do"""
    print("\n" + "="*60)
    print("TEST 4: API Endpoints Simulation")
    print("="*60)
    
    # Simulate /api/translate-text
    print("\nEndpoint: POST /api/translate-text")
    print("Request: {\"text\": \"Hello, world!\"}")
    translator = EnglishKannadaTranslator()
    result = translator.translate_text("Hello, world!")
    print(f"Response: {{\"success\": true, \"english\": \"Hello, world!\", \"kannada\": \"{result}\"}}")
    
    # Simulate /api/speech-to-text
    print("\nEndpoint: POST /api/speech-to-text")
    print("Request: FormData with audio file")
    print("Response: {\"success\": true, \"text\": \"[recognized text]\"}")
    
    # Simulate /api/translate-with-speech
    print("\nEndpoint: POST /api/translate-with-speech")
    print("Request: {\"text\": \"Hello, world!\"}")
    print(f"Response: {{\"success\": true, \"kannada\": \"{result}\", \"audio\": \"[base64-audio]\"}}")
    
    # Simulate /api/full-translation
    print("\nEndpoint: POST /api/full-translation")
    print("Request: FormData with audio file")
    print(f"Response: {{\"success\": true, \"english\": \"[...]\", \"kannada\": \"{result}\", \"audio\": \"[base64-audio]\"}}")
    
    print("\n✓ API endpoint simulation completed")


def test_configuration():
    """Test current configuration"""
    print("\n" + "="*60)
    print("TEST 5: Configuration Check")
    print("="*60)
    
    print("\n✓ Python Version:", sys.version.split()[0])
    print("✓ Project Path:", Path(__file__).parent)
    
    # Check if required modules are available
    modules = ['flask', 'speech_recognition', 'gtts', 'pyttsx3']
    print("\nDependencies:")
    for module in modules:
        try:
            __import__(module)
            print(f"  ✓ {module} installed")
        except ImportError:
            print(f"  ✗ {module} NOT installed (run: pip install -r requirements.txt)")
    
    print("\n✓ Configuration check completed")


def interactive_mode():
    """Interactive translation mode"""
    print("\n" + "="*60)
    print("INTERACTIVE MODE: Manual Translation Test")
    print("="*60)
    print("\nEnter text to translate (or 'quit' to exit):\n")
    
    translator = EnglishKannadaTranslator()
    
    while True:
        try:
            english_text = input("English: ").strip()
            
            if english_text.lower() == 'quit':
                print("\nExiting interactive mode...")
                break
            
            if not english_text:
                continue
            
            kannada_text = translator.translate_text(english_text)
            print(f"Kannada: {kannada_text}\n")
        
        except KeyboardInterrupt:
            print("\n\nExiting interactive mode...")
            break
        except Exception as e:
            print(f"Error: {e}\n")


def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  English to Kannada Translator - Test Suite".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    
    try:
        test_configuration()
        test_text_translation()
        test_speech_output()
        test_full_translation_flow()
        test_api_endpoints_simulation()
        
        print("\n" + "="*60)
        print("ALL TESTS COMPLETED SUCCESSFULLY ✓")
        print("="*60)
        
        # Ask if user wants interactive mode
        print("\nWould you like to try interactive mode? (yes/no): ", end="")
        if input().strip().lower() in ['yes', 'y']:
            interactive_mode()
        
    except Exception as e:
        print(f"\n✗ Test Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--interactive":
            interactive_mode()
        elif sys.argv[1] == "--help":
            print("""
Usage: python test_example.py [option]

Options:
  (no arguments)     Run all tests
  --interactive      Interactive translation mode
  --help            Show this help message

Examples:
  python test_example.py           # Run all tests
  python test_example.py --interactive  # Interactive mode
            """)
    else:
        run_all_tests()
