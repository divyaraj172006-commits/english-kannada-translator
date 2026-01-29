# Quick Start Guide - English to Kannada Translator

## 5-Minute Setup

### Step 1: Install Dependencies (2 minutes)
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application (1 minute)

**Option A - Windows:**
```bash
run.bat
```

**Option B - Mac/Linux:**
```bash
bash run.sh
```

**Option C - Manual:**
```bash
python app.py
```

### Step 3: Open in Browser (1 minute)
- Visit: `http://localhost:5000`
- You'll see the translator interface

### Step 4: Start Translating! (1 minute)
- Choose a translation mode from the tabs
- Enter text or upload audio
- Click the appropriate button
- View and copy your results

---

## Basic Usage Examples

### Text Translation
```
Input:  "Hello, how are you?"
Output: "ನಮಸ್ಕಾರ, ನೀವು ಹೇಗಿದ್ದೀರಿ?"
```

### Speech to Text
1. Upload an English speech audio file
2. Get the recognized English text
3. Optionally translate to Kannada

### Text to Speech
1. Enter English text
2. Get Kannada translation
3. Listen to Kannada pronunciation

### Full Speech Translation
1. Upload English speech audio
2. Get English transcript
3. Get Kannada translation
4. Listen to Kannada audio

---

## Advanced Setup (Optional)

### Enable Full Google Cloud Features

1. **Create Google Cloud Project**
   - Go to https://console.cloud.google.com
   - Create a new project
   - Enable Translation and Speech-to-Text APIs

2. **Create Service Account**
   - Go to Service Accounts
   - Create new service account
   - Download JSON key

3. **Set Credentials**
```bash
# Windows PowerShell
$env:GOOGLE_APPLICATION_CREDENTIALS = "C:\path\to\credentials.json"

# Windows Command Prompt
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\credentials.json

# Mac/Linux
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```

4. **Restart Application**
```bash
python app.py
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Port 5000 Already in Use
**Solution:** Edit `app.py` and change:
```python
app.run(debug=True, port=5001)  # Change 5000 to another port
```

### Issue: Google Cloud APIs Not Available
**Solution:**
- Application will use basic dictionary translation
- Or set up Google Cloud credentials (see Advanced Setup above)

### Issue: Audio Files Not Playing
**Solution:**
- Try a different audio format (MP3, WAV, OGG)
- Check your browser's audio support
- Ensure speaker volume is turned on

---

## Features Breakdown

### 🎯 Text Translation Tab
- **Best for**: Quick text translations
- **Input**: Type or paste English text
- **Output**: Kannada translation
- **Features**: Copy button for easy sharing

### 🎤 Speech to Text Tab
- **Best for**: Converting English audio to text
- **Input**: Upload audio file
- **Output**: Recognized English text
- **Features**: Automatic transcription

### 🔊 Text with Speech Output Tab
- **Best for**: Hearing Kannada pronunciation
- **Input**: Type English text
- **Output**: Kannada translation + audio
- **Features**: Embedded audio player

### 🎙️ Full Speech Translation Tab
- **Best for**: Complete speech-to-speech translation
- **Input**: Upload English speech audio
- **Output**: English text + Kannada translation + Kannada audio
- **Features**: Full pipeline in one click

---

## File Structure Overview

```
app.py                    ← Main Flask application (START HERE)
run.bat / run.sh          ← Startup scripts
requirements.txt          ← Python dependencies
.env.example             ← Configuration template

templates/
└── index.html           ← Web interface

static/
├── css/
│   └── style.css        ← Styling (responsive design)
└── js/
    └── script.js        ← Frontend logic

src/
├── translator.py        ← Translation logic
├── speech_input.py      ← Speech recognition
└── speech_output.py     ← Text-to-speech
```

---

## Common Commands

### Start Development Server
```bash
python app.py
```

### Check Installed Packages
```bash
pip list
```

### Update All Packages
```bash
pip install --upgrade -r requirements.txt
```

### Reinstall Requirements
```bash
pip install -r requirements.txt --force-reinstall
```

---

## API Quick Reference

### Translate Text
```bash
curl -X POST http://localhost:5000/api/translate-text \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello"}'
```

### Speech to Text
```bash
curl -X POST http://localhost:5000/api/speech-to-text \
  -F "audio=@audio.mp3"
```

### Translate with Speech
```bash
curl -X POST http://localhost:5000/api/translate-with-speech \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello"}'
```

### Full Translation
```bash
curl -X POST http://localhost:5000/api/full-translation \
  -F "audio=@audio.mp3"
```

---

## Performance Tips

1. **Use MP3 files** for audio (faster processing)
2. **Keep text short** for better accuracy
3. **Use clear audio** for speech recognition
4. **Enable offline mode** for faster response (use pyttsx3)
5. **Cache results** for frequently translated phrases

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Run the application
3. ✅ Try basic text translation
4. ✅ Test speech features
5. ⭐ Set up Google Cloud (optional)

---

## Support & Help

**Need Help?**
1. Check the main [README.md](README.md)
2. Review error messages in terminal
3. Ensure internet connection for API features
4. Verify audio files are in supported format

**Found an Issue?**
- Check the Troubleshooting section
- Verify all dependencies are installed
- Check if Google APIs are accessible

---

## Keyboard Shortcuts

- `Ctrl+Enter` in text area → Submit for translation
- `Ctrl+C` in terminal → Stop the server
- `Click audio player` → Play/pause speech output

---

**You're all set! Enjoy translating! 🌐**
