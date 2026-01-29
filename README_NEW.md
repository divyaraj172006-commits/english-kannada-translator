# English to Kannada Translator

A Python-based translator application that converts English text and speech to Kannada with text and speech output capabilities.

## Features

- **Text Translation**: Translate English text to Kannada
- **Speech Recognition**: Convert spoken English to text
- **Text-to-Speech**: Hear translations in Kannada
- **Multiple Modes**:
  - Pure text translation
  - Speech input with text output
  - Text input with speech output
  - Full end-to-end speech translation

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Microphone for speech input (optional)

### Setup

1. Clone or download this repository
2. Navigate to the project directory:
```bash
cd english-kannada-translator
```

3. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv env

# Activate on Windows (PowerShell)
.\env\Scripts\Activate.ps1

# Activate on Windows (Command Prompt)
env\Scripts\activate.bat

# Activate on macOS/Linux
source env/bin/activate
```

4. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Additional Setup for Google Cloud Translation

For full translation capabilities, you may need to set up Google Cloud credentials:
1. Create a Google Cloud project
2. Enable the Translation API
3. Download service account credentials JSON
4. Set the environment variable:
```bash
# Windows PowerShell
$env:GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"

# Windows Command Prompt
set GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json

# macOS/Linux
export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
```

## Usage

### Running the Application

```bash
python main.py
```

This will launch an interactive menu with the following options:

1. **Translate Text** - Enter English text and get Kannada translation
2. **Translate from Speech** - Speak in English, get Kannada translation
3. **Translate Text with Speech Output** - Type English, hear Kannada translation
4. **Full Translation** - Speak English, hear Kannada translation
5. **Exit** - Close the application

### Using as a Module

You can also use the translator in your own Python code:

```python
from src.translator import EnglishKannadaTranslator
from src.speech_input import SpeechInput
from src.speech_output import SpeechOutput

# Text translation
translator = EnglishKannadaTranslator()
result = translator.translate_text("Hello, how are you?")
print(result)  # ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?

# Speech input
speech_input = SpeechInput()
text = speech_input.record_from_microphone()

# Speech output
speech_output = SpeechOutput()
speech_output.speak("ನಮಸ್ಕಾರ", language='kn')
```

## Project Structure

```
english-kannada-translator/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── env/                   # Virtual environment (created after setup)
└── src/
    ├── translator.py      # Core translation module
    ├── speech_input.py    # Speech recognition module
    └── speech_output.py   # Text-to-speech module
```

## Dependencies

- **google-cloud-translate**: For text translation via Google Cloud API
- **SpeechRecognition**: For speech-to-text conversion
- **gTTS**: For text-to-speech synthesis
- **pyttsx3**: For offline text-to-speech
- **pyaudio**: For audio input/output handling (optional, for enhanced audio support)

## Limitations

- **Translation**: Without Google Cloud credentials, falls back to a limited dictionary-based translation
- **Speech Recognition**: Requires internet connection for Google Speech Recognition
- **Text-to-Speech**: Google TTS requires internet connection; pyttsx3 works offline but with limited language support
- **Microphone**: Speech input requires a working microphone

## Troubleshooting

### Virtual Environment Activation Issues (Windows PowerShell)
If you get an error about module 'env', use the correct script:
```bash
# Correct way for PowerShell
.\env\Scripts\Activate.ps1

# For Command Prompt
env\Scripts\activate.bat
```

If you still get permission errors in PowerShell, run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ImportError for PyAudio on Windows
If you encounter PyAudio issues on Windows:
```bash
pip install pipwin
pipwin install pyaudio
```

### No module named 'google.cloud'
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Audio not working
- Check if your microphone is connected and working
- Verify audio drivers are installed
- Try running with `method='local'` for offline TTS

## Usage Examples

### Example 1: Simple Text Translation
```python
from src.translator import EnglishKannadaTranslator

translator = EnglishKannadaTranslator()
print(translator.translate_text("Thank you"))  # ಧನ್ಯವಾದ
```

### Example 2: Translate with Voice Output
```python
from src.translator import EnglishKannadaTranslator
from src.speech_output import SpeechOutput

translator = EnglishKannadaTranslator()
speech = SpeechOutput()

text = "Hello, how are you?"
kannada = translator.translate_text(text)
speech.speak(kannada, language='kn')
```

### Example 3: Voice to Voice Translation
```python
from src.translator import EnglishKannadaTranslator
from src.speech_input import SpeechInput
from src.speech_output import SpeechOutput

translator = EnglishKannadaTranslator()
speech_input = SpeechInput()
speech_output = SpeechOutput()

english_text = speech_input.record_from_microphone()
kannada_text = translator.translate_text(english_text)
speech_output.speak(kannada_text, language='kn')
```

## Future Enhancements

- Support for more languages
- GUI interface using Tkinter or PyQt
- File-based audio input/output
- Real-time translation
- Offline translation model
- Custom dictionary support
- Language detection
- Batch file processing

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork, modify, and improve this project!

## Support

For issues and questions, please check the documentation or review the code comments.
