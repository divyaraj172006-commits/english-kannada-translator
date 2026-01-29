# English to Kannada Translator

A comprehensive web-based translator application that supports both text and speech translation between English and Kannada using Flask, HTML, and CSS.

## Features

✨ **Text Translation** - Translate English text to Kannada
🎤 **Speech to Text** - Convert English speech to text (upload audio files)
🔊 **Text with Speech Output** - Translate text and listen to Kannada pronunciation
🎙️ **Full Speech Translation** - Complete speech-to-speech translation (speech to text to speech)

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Translation API**: Google Cloud Translation
- **Speech Recognition**: Google Speech Recognition API
- **Text-to-Speech**: Google Text-to-Speech (gTTS)

## Project Structure

```
english-kannada-translator/
├── app.py                  # Main Flask application
├── main.py                 # CLI version (legacy)
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/
│   └── index.html         # Main web interface
├── static/
│   ├── css/
│   │   └── style.css      # Styling (2000+ lines)
│   └── js/
│       └── script.js      # Frontend logic
└── src/
    ├── translator.py      # Translation logic
    ├── speech_input.py    # Speech recognition
    └── speech_output.py   # Text-to-speech
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Microphone (for real-time speech input)
- Internet connection (for API services)

### Setup Steps

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Set up Google Cloud Credentials** (Optional but recommended for full functionality)
   - Create a project on Google Cloud Console
   - Enable Translation API and Speech-to-Text API
   - Download credentials JSON file
   - Set environment variable:
   ```bash
   # On Windows (PowerShell)
   $env:GOOGLE_APPLICATION_CREDENTIALS = "path/to/credentials.json"
   
   # On Windows (Command Prompt)
   set GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
   
   # On Mac/Linux
   export GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
   ```

3. **Run the Flask application**
```bash
python app.py
```

4. **Access the web interface**
   - Open your browser and go to: `http://localhost:5000`
   - The interface will open automatically or navigate manually to the URL

## Usage Guide

### 1. Text Translation Tab
- **Step 1**: Enter English text in the textarea
- **Step 2**: Click "Translate" button
- **Step 3**: View the Kannada translation
- **Step 4**: Click "Copy Kannada" to copy the result

### 2. Speech to Text Tab
- **Step 1**: Upload an audio file (MP3, WAV, OGG, FLAC, etc.)
- **Step 2**: Click "Convert Speech to Text"
- **Step 3**: View the recognized English text
- **Step 4**: Text is automatically copied on demand

### 3. Text with Speech Output Tab
- **Step 1**: Enter English text
- **Step 2**: Click "Translate & Play Audio"
- **Step 3**: View the translation
- **Step 4**: Listen to the Kannada pronunciation using the audio player
- **Step 5**: Copy the translation if needed

### 4. Full Speech Translation Tab
- **Step 1**: Upload an audio file
- **Step 2**: Click "Process & Translate"
- **Step 3**: Get the recognized English text
- **Step 4**: View the Kannada translation
- **Step 5**: Listen to the Kannada audio
- **Step 6**: Copy the translation

## API Endpoints

### POST `/api/translate-text`
Translate English text to Kannada
```json
Request: {"text": "Hello, how are you?"}
Response: {
  "success": true,
  "english": "Hello, how are you?",
  "kannada": "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?"
}
```

### POST `/api/speech-to-text`
Convert speech from audio file to text
```json
Request: FormData with audio file
Response: {
  "success": true,
  "text": "Hello, how are you?"
}
```

### POST `/api/translate-with-speech`
Translate text and generate speech
```json
Request: {"text": "Hello, how are you?"}
Response: {
  "success": true,
  "english": "Hello, how are you?",
  "kannada": "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?",
  "audio": "base64-encoded-mp3-data"
}
```

### POST `/api/full-translation`
Full speech-to-speech translation
```json
Request: FormData with audio file
Response: {
  "success": true,
  "english": "Hello, how are you?",
  "kannada": "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?",
  "audio": "base64-encoded-mp3-data"
}
```

## Configuration

### Flask Configuration (app.py)
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'              # Upload directory
```

### Environment Variables
```bash
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
FLASK_ENV=development
FLASK_DEBUG=1
```

## Features Explained

### Frontend Features
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Tab-Based Interface**: Easy navigation between different translation modes
- **Real-Time Feedback**: Loading indicators and error messages
- **Audio Player**: Built-in audio player for speech output
- **Copy Functionality**: Easy copy-to-clipboard feature
- **Dark Mode Support**: Gradient UI with modern styling

### Backend Features
- **API-Based Architecture**: RESTful endpoints for all operations
- **Error Handling**: Comprehensive error handling and validation
- **File Management**: Automatic cleanup of temporary files
- **Fallback Translation**: Dictionary-based translation when APIs unavailable
- **Multiple TTS Methods**: Google (online) and pyttsx3 (offline) support

## Troubleshooting

### Issue: "No module named 'google.cloud'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: pyaudio Installation Fails on Windows
**Solution**: pyaudio is optional (only needed for microphone input). The web app works fine without it!
- Option A: Skip it (already commented out in requirements.txt)
  ```bash
  pip install -r requirements.txt
  ```
- Option B: Use pre-built wheels
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```
- Option C: Install on Windows with conda
  ```bash
  conda install pyaudio
  ```
**Solution**: 
- Check internet connection
- Verify audio file format (try MP3 or WAV)
- Check Google Speech API accessibility

### Issue: Audio Not Playing
**Solution**:
- Verify browser supports HTML5 audio
- Check speaker/audio output device
- Try different audio format

### Issue: Translation Returns Original Text
**Solution**:
- Without Google Cloud credentials, basic dictionary translation is used
- Set up proper Google Cloud credentials for full translation
- Check if 'translatedText' or 'translations' field in API response

### Issue: CORS Errors
**Solution**:
- For production, configure CORS appropriately
- The default Flask setup works for localhost

## Performance Optimization

1. **Use Compressed Audio**: Smaller files process faster
2. **Local TTS**: For offline use, configure pyttsx3
3. **Batch Requests**: Group multiple translations
4. **Cache Results**: Implement caching for repeated phrases

## Browser Support

| Browser | Desktop | Mobile |
|---------|---------|--------|
| Chrome  | ✅      | ✅     |
| Firefox | ✅      | ✅     |
| Safari  | ✅      | ✅     |
| Edge    | ✅      | ✅     |

## Security Notes

⚠️ **Important Security Considerations**:

1. **File Uploads**: 
   - Limited to 16MB
   - Validated before processing
   - Temporary files auto-deleted

2. **API Keys**:
   - Never hardcode credentials
   - Use environment variables
   - Rotate credentials regularly

3. **HTTPS**:
   - Use HTTPS in production
   - Implement proper CORS headers
   - Add authentication if needed

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0.0 | Web framework |
| google-cloud-translate | 3.14.1 | Translation API |
| SpeechRecognition | 3.10.0 | Speech recognition |
| gTTS | 2.3.2 | Text-to-speech |
| pyttsx3 | 2.90 | Offline TTS |
| pyaudio | 0.2.13 | Audio input |
| Werkzeug | 3.0.1 | WSGI utilities |

## Future Enhancements

- [ ] Multiple language support (not just Kannada)
- [ ] User authentication and history
- [ ] Real-time speech translation
- [ ] Document translation
- [ ] Translation accuracy scoring
- [ ] Custom dictionary support
- [ ] Offline mode improvements

## Common Use Cases

1. **Language Learning**: Practice English to Kannada pronunciation
2. **Business Communication**: Quick document/email translation
3. **Content Creation**: Generate multilingual content
4. **Accessibility**: Provide translations for accessibility needs
5. **Research**: Analyze translated content

## Resources

- [Google Cloud Translation API](https://cloud.google.com/translate)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Kannada Language Info](https://en.wikipedia.org/wiki/Kannada_language)
- [HTML Audio Reference](https://www.w3schools.com/html/html5_audio.asp)

## License

This project is open source. Feel free to use, modify, and distribute.

## Author

English to Kannada Translator Application
- Built with Flask, HTML5, CSS3, and JavaScript
- Powered by Google Cloud APIs

---

**Last Updated**: January 2024
**Version**: 1.0.0
**Status**: Production Ready ✅