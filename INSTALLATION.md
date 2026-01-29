# Installation Instructions

## Prerequisites

Ensure you have the following installed on your system:

1. **Python 3.7 or Higher**
   - Download from: https://www.python.org/downloads/
   - Verify installation: `python --version` or `python3 --version`

2. **pip (Python Package Manager)**
   - Usually comes with Python
   - Verify: `pip --version` or `pip3 --version`

3. **Internet Connection** (required for API services)

4. **(Optional) FFmpeg** (for advanced audio processing)
   - Windows: `choco install ffmpeg`
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`

---

## Installation Steps

### Step 1: Navigate to Project Directory
```bash
cd c:\Users\divya\OneDrive\Desktop\english-kannada-translator\english-kannada-translator
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- `flask` - Web framework
- `google-cloud-translate` - Translation service
- `SpeechRecognition` - Speech recognition
- `gTTS` - Text-to-speech
- `pyttsx3` - Offline text-to-speech
- `pyaudio` - Audio processing
- `Werkzeug` - WSGI utilities

---

## Dependency Details

| Package | Version | Purpose | Required |
|---------|---------|---------|----------|
| flask | 3.0.0 | Web server framework | ✅ Yes |
| google-cloud-translate | 3.14.1 | Translation API | ✅ Yes |
| SpeechRecognition | 3.10.0 | Speech-to-text | ✅ Yes |
| gTTS | 2.3.2 | Text-to-speech | ✅ Yes |
| pyttsx3 | 2.90 | Offline TTS | ✅ Yes |
| pyaudio | 0.2.13 | Audio input/output | ⚠️ Optional* |
| Werkzeug | 3.0.1 | WSGI utilities | ✅ Yes |
| python-dotenv | 1.0.0 | Environment config | ✅ Yes |

*Note: pyaudio is optional but recommended for microphone input

---

## OS-Specific Installation Issues

### Windows Installation

#### Issue: pyaudio installation fails
**Solution A - Use pre-built wheels:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Solution B - Skip pyaudio (if not using microphone):**
Edit `requirements.txt` to remove pyaudio line, then:
```bash
pip install -r requirements.txt
```

#### Issue: Google Cloud libraries fail
**Solution:**
```bash
pip install google-cloud-translate --upgrade
```

### Mac Installation

#### Issue: pyaudio needs Xcode
**Solution:**
```bash
xcode-select --install
brew install portaudio
pip install pyaudio
```

#### Issue: gTTS connection issues
**Solution:**
```bash
pip install --upgrade gTTS
```

### Linux Installation (Ubuntu/Debian)

#### Required system packages:
```bash
sudo apt-get install python3-dev
sudo apt-get install portaudio19-dev
sudo apt-get install ffmpeg
```

#### Then install Python packages:
```bash
pip3 install -r requirements.txt
```

#### Issue: Permission denied
**Solution:**
```bash
pip3 install --user -r requirements.txt
```

---

## Verification

### Verify Installation
```bash
python -c "import flask; import speech_recognition; import gTTS; print('All packages installed successfully!')"
```

### Check Individual Packages
```bash
# Flask
python -c "import flask; print(f'Flask version: {flask.__version__}')"

# SpeechRecognition
python -c "import speech_recognition; print('SpeechRecognition installed')"

# gTTS
python -c "from gtts import gTTS; print('gTTS installed')"

# Google Cloud
python -c "from google.cloud import translate_v2; print('Google Cloud installed')"
```

---

## Google Cloud Setup (Optional but Recommended)

### Create Service Account
1. Go to https://console.cloud.google.com
2. Create a new project
3. Enable APIs:
   - Google Cloud Translation API
   - Google Cloud Speech-to-Text API
4. Create Service Account
5. Generate JSON key file

### Configure Credentials
```bash
# Windows PowerShell
$env:GOOGLE_APPLICATION_CREDENTIALS = "path\to\credentials.json"

# Windows CMD
set GOOGLE_APPLICATION_CREDENTIALS=path\to\credentials.json

# Mac/Linux
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```

### Test Connection
```bash
python -c "from google.cloud import translate_v2; client = translate_v2.Client(); print('Google Cloud connected!')"
```

---

## Virtual Environment Management

### Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Deactivate Virtual Environment
```bash
deactivate
```

### Recreate Virtual Environment
```bash
# Delete existing
rmdir /s venv          # Windows
rm -rf venv            # Mac/Linux

# Create new
python -m venv venv
```

---

## Troubleshooting Installation

### Issue: "No module named 'flask'"
```bash
pip install flask==3.0.0
```

### Issue: "pip not found"
```bash
# Try pip3
pip3 install -r requirements.txt

# Or reinstall pip
python -m pip install --upgrade pip
```

### Issue: Permission denied
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use sudo (not recommended)
sudo pip install -r requirements.txt
```

### Issue: SSL Certificate Error
```bash
pip install --trusted-host pypi.python.org -r requirements.txt
```

### Issue: Dependency conflicts
```bash
# Create fresh virtual environment
python -m venv fresh_venv
source fresh_venv/bin/activate
pip install -r requirements.txt
```

---

## Upgrading Packages

### Upgrade Individual Package
```bash
pip install --upgrade flask
```

### Upgrade All Packages
```bash
pip install --upgrade -r requirements.txt
```

### Update requirements.txt
```bash
pip freeze > requirements.txt
```

---

## Development Setup

### Install Development Tools (Optional)
```bash
pip install black
pip install pylint
pip install pytest
pip install pytest-flask
```

### Run Tests
```bash
pytest tests/
```

### Format Code
```bash
black .
```

---

## System Requirements

| Aspect | Minimum | Recommended |
|--------|---------|------------|
| Python | 3.7 | 3.10+ |
| RAM | 2GB | 4GB+ |
| Disk | 500MB | 1GB+ |
| Internet | Required | Always on |
| CPU | 1 Core | 2+ Cores |

---

## Success Checklist

After installation, verify:
- [ ] Python installed and accessible
- [ ] pip working correctly
- [ ] Virtual environment created
- [ ] Requirements installed without errors
- [ ] Flask can be imported
- [ ] Speech libraries installed
- [ ] Google Cloud SDK configured (optional)
- [ ] Application starts without errors

---

## Getting Help

If installation fails:

1. **Check Python version** - Must be 3.7+
2. **Verify pip** - Run `pip --version`
3. **Read error messages** - They often suggest solutions
4. **Try virtual environment** - Isolates package issues
5. **Check internet** - Required for downloads
6. **Look at OS-specific section** - Above for your OS

---

## Next Steps

After successful installation:
1. Run `python app.py`
2. Open `http://localhost:5000`
3. Test basic translation
4. Try speech features

See [QUICKSTART.md](QUICKSTART.md) for usage guide!

---

**Installation completed! 🎉**
