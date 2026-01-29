@echo off
REM English to Kannada Translator Startup Script for Windows

echo ============================================
echo  English to Kannada Translator
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ and add it to PATH
    pause
    exit /b 1
)

echo Checking Python installation...
python --version
echo.

REM Check if requirements are installed
echo Checking dependencies...
pip list | findstr flask >nul 2>&1
if errorlevel 1 (
    echo Installing requirements...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install requirements
        pause
        exit /b 1
    )
)

echo.
echo Starting Flask application...
echo Opening browser at http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the Flask app
python app.py

pause
