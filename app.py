"""
Flask Application for English to Kannada Translator
Supports text and speech translation
"""

import sys
from pathlib import Path
from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import base64

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from translator import EnglishKannadaTranslator
from speech_input import SpeechInput
from speech_output import SpeechOutput

# Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize translator and speech modules
translator = EnglishKannadaTranslator()
speech_input = SpeechInput()
speech_output = SpeechOutput(method='google')


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/translate-text', methods=['POST'])
def translate_text():
    """
    API endpoint for text translation
    Expects: {"text": "English text to translate"}
    Returns: {"kannada": "Translated Kannada text", "success": true}
    """
    try:
        data = request.json
        english_text = data.get('text', '').strip()
        
        if not english_text:
            return jsonify({'success': False, 'error': 'No text provided'}), 400
        
        # Translate the text
        kannada_text = translator.translate_text(english_text)
        
        return jsonify({
            'success': True,
            'english': english_text,
            'kannada': kannada_text
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/translate-with-speech', methods=['POST'])
def translate_with_speech():
    """
    API endpoint for text translation with speech output
    Expects: {"text": "English text to translate"}
    Returns: Audio file as base64
    """
    try:
        data = request.json
        english_text = data.get('text', '').strip()
        
        if not english_text:
            return jsonify({'success': False, 'error': 'No text provided'}), 400
        
        # Translate the text
        kannada_text = translator.translate_text(english_text)
        
        # Generate speech for Kannada text
        audio_path = speech_output.speak_and_save(kannada_text, language='kn')
        
        # Read and encode audio file as base64
        if audio_path and os.path.exists(audio_path):
            with open(audio_path, 'rb') as f:
                audio_base64 = base64.b64encode(f.read()).decode('utf-8')
            
            # Clean up the temporary file
            try:
                os.remove(audio_path)
            except:
                pass
            
            return jsonify({
                'success': True,
                'english': english_text,
                'kannada': kannada_text,
                'audio': audio_base64
            })
        
        return jsonify({
            'success': True,
            'english': english_text,
            'kannada': kannada_text,
            'message': 'Translation successful but audio generation failed'
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/speech-to-text', methods=['POST'])
def speech_to_text():
    """
    API endpoint for speech-to-text conversion
    Expects: Audio file in request
    Returns: {"text": "Recognized English text", "success": true}
    """
    try:
        if 'audio' not in request.files:
            return jsonify({'success': False, 'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        if audio_file.filename == '':
            return jsonify({'success': False, 'error': 'No audio file selected'}), 400
        
        # Save uploaded file
        filename = secure_filename(audio_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(filepath)
        
        # Recognize speech
        text = speech_input.recognize_from_file(filepath)
        
        # Clean up the file
        try:
            os.remove(filepath)
        except:
            pass
        
        if text:
            return jsonify({
                'success': True,
                'text': text
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Could not recognize speech'
            }), 400
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/full-translation', methods=['POST'])
def full_translation():
    """
    API endpoint for full speech-to-speech translation
    Expects: Audio file in request
    Returns: {"english": "...", "kannada": "...", "audio": "base64...", "success": true}
    """
    try:
        if 'audio' not in request.files:
            return jsonify({'success': False, 'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        if audio_file.filename == '':
            return jsonify({'success': False, 'error': 'No audio file selected'}), 400
        
        # Save uploaded file
        filename = secure_filename(audio_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(filepath)
        
        # Step 1: Recognize English speech
        english_text = speech_input.recognize_from_file(filepath)
        
        # Clean up the file
        try:
            os.remove(filepath)
        except:
            pass
        
        if not english_text:
            return jsonify({
                'success': False,
                'error': 'Could not recognize speech from audio'
            }), 400
        
        # Step 2: Translate to Kannada
        kannada_text = translator.translate_text(english_text)
        
        # Step 3: Generate speech for Kannada text
        audio_path = speech_output.speak_and_save(kannada_text, language='kn')
        
        audio_base64 = None
        if audio_path and os.path.exists(audio_path):
            with open(audio_path, 'rb') as f:
                audio_base64 = base64.b64encode(f.read()).decode('utf-8')
            
            try:
                os.remove(audio_path)
            except:
                pass
        
        return jsonify({
            'success': True,
            'english': english_text,
            'kannada': kannada_text,
            'audio': audio_base64
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
