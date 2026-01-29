// Tab Switching
function switchTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => {
        tab.classList.remove('active');
    });

    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(btn => {
        btn.classList.remove('active');
    });

    // Show selected tab
    document.getElementById(tabName).classList.add('active');

    // Add active class to clicked button
    event.target.classList.add('active');
}

// Loading Spinner
function showLoading(show = true) {
    const loading = document.getElementById('loading');
    loading.style.display = show ? 'flex' : 'none';
}

// Error Handler
function showError(elementId, message) {
    const errorDiv = document.getElementById(elementId);
    if (errorDiv) {
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }
}

function hideError(elementId) {
    const errorDiv = document.getElementById(elementId);
    if (errorDiv) {
        errorDiv.style.display = 'none';
    }
}

// Copy to Clipboard
function copyToClipboard(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        const text = element.textContent;
        navigator.clipboard.writeText(text).then(() => {
            alert('Copied to clipboard!');
        }).catch(err => {
            console.error('Failed to copy:', err);
        });
    }
}

// Tab 1: Translate Text
async function translateText() {
    const englishText = document.getElementById('english-text').value.trim();

    if (!englishText) {
        showError('text-error', 'Please enter some English text to translate.');
        return;
    }

    hideError('text-error');
    showLoading(true);

    try {
        const response = await fetch('/api/translate-text', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: englishText })
        });

        const data = await response.json();

        if (data.success) {
            document.getElementById('result-english').textContent = data.english;
            document.getElementById('result-kannada').textContent = data.kannada;
            document.getElementById('text-result').style.display = 'block';
            hideError('text-error');
        } else {
            showError('text-error', data.error || 'Translation failed. Please try again.');
            document.getElementById('text-result').style.display = 'none';
        }
    } catch (error) {
        showError('text-error', 'Error: ' + error.message);
        document.getElementById('text-result').style.display = 'none';
    } finally {
        showLoading(false);
    }
}

// Tab 2: Speech to Text
async function speechToText() {
    const audioFile = document.getElementById('audio-file').files[0];

    if (!audioFile) {
        showError('speech-error', 'Please select an audio file.');
        return;
    }

    hideError('speech-error');
    showLoading(true);

    const formData = new FormData();
    formData.append('audio', audioFile);

    try {
        const response = await fetch('/api/speech-to-text', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            document.getElementById('result-recognized').textContent = data.text;
            document.getElementById('speech-result').style.display = 'block';
            hideError('speech-error');
        } else {
            showError('speech-error', data.error || 'Speech recognition failed. Please try again.');
            document.getElementById('speech-result').style.display = 'none';
        }
    } catch (error) {
        showError('speech-error', 'Error: ' + error.message);
        document.getElementById('speech-result').style.display = 'none';
    } finally {
        showLoading(false);
    }
}

// Tab 3: Text with Speech Output
async function translateWithSpeech() {
    const englishText = document.getElementById('text-speech-input').value.trim();

    if (!englishText) {
        showError('text-speech-error', 'Please enter some English text to translate.');
        return;
    }

    hideError('text-speech-error');
    showLoading(true);

    try {
        const response = await fetch('/api/translate-with-speech', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: englishText })
        });

        const data = await response.json();

        if (data.success) {
            document.getElementById('result-english-speech').textContent = data.english;
            document.getElementById('result-kannada-speech').textContent = data.kannada;

            if (data.audio) {
                const audioData = 'data:audio/mp3;base64,' + data.audio;
                document.getElementById('audio-element').src = audioData;
                document.getElementById('audio-player').style.display = 'block';
            } else {
                document.getElementById('audio-player').style.display = 'none';
            }

            document.getElementById('text-speech-result').style.display = 'block';
            hideError('text-speech-error');
        } else {
            showError('text-speech-error', data.error || 'Translation failed. Please try again.');
            document.getElementById('text-speech-result').style.display = 'none';
        }
    } catch (error) {
        showError('text-speech-error', 'Error: ' + error.message);
        document.getElementById('text-speech-result').style.display = 'none';
    } finally {
        showLoading(false);
    }
}

// Tab 4: Full Speech Translation
async function fullTranslation() {
    const audioFile = document.getElementById('full-audio-file').files[0];

    if (!audioFile) {
        showError('full-error', 'Please select an audio file.');
        return;
    }

    hideError('full-error');
    showLoading(true);

    const formData = new FormData();
    formData.append('audio', audioFile);

    try {
        const response = await fetch('/api/full-translation', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            document.getElementById('result-full-english').textContent = data.english;
            document.getElementById('result-full-kannada').textContent = data.kannada;

            if (data.audio) {
                const audioData = 'data:audio/mp3;base64,' + data.audio;
                document.getElementById('full-audio-element').src = audioData;
                document.getElementById('full-audio-player').style.display = 'block';
            } else {
                document.getElementById('full-audio-player').style.display = 'none';
            }

            document.getElementById('full-result').style.display = 'block';
            hideError('full-error');
        } else {
            showError('full-error', data.error || 'Translation failed. Please try again.');
            document.getElementById('full-result').style.display = 'none';
        }
    } catch (error) {
        showError('full-error', 'Error: ' + error.message);
        document.getElementById('full-result').style.display = 'none';
    } finally {
        showLoading(false);
    }
}

// Handle Enter key in textareas
document.addEventListener('DOMContentLoaded', function () {
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('keydown', function (e) {
            // Allow normal behavior (Shift+Enter for new line, Enter+Ctrl for submit)
            if (e.ctrlKey && e.key === 'Enter') {
                const btn = this.parentElement.nextElementSibling;
                if (btn && btn.classList.contains('btn')) {
                    btn.click();
                }
            }
        });
    });
});
