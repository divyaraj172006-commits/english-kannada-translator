#!/bin/bash
# English to Kannada Translator Startup Script for Mac/Linux

echo "============================================"
echo " English to Kannada Translator"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.7+ using:"
    echo "  - macOS: brew install python3"
    echo "  - Linux: sudo apt-get install python3"
    exit 1
fi

echo "Checking Python installation..."
python3 --version
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed"
    echo "Please install pip3"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
pip3 list | grep -q flask || {
    echo "Installing requirements..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install requirements"
        exit 1
    fi
}

echo ""
echo "Starting Flask application..."
echo "Opening browser at http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the Flask app
python3 app.py
