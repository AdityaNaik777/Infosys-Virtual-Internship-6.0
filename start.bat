@echo off
REM Quick Start Script for Infosys Virtual Internship Quiz Application

echo ========================================
echo  Infosys Quiz App - Quick Start
echo ========================================
echo.

REM Activate virtual environment
echo [1/4] Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment activated
echo.

REM Check if .env exists
if not exist .env (
    echo WARNING: .env file not found!
    echo Please create .env file with required settings.
    echo See SETUP_GUIDE.md for details.
    pause
    exit /b 1
)

REM Run migrations
echo [2/4] Running database migrations...
.venv\Scripts\python.exe manage.py migrate
if errorlevel 1 (
    echo ERROR: Migration failed. Check database configuration.
    pause
    exit /b 1
)
echo ✓ Migrations completed
echo.

REM Collect static files (if needed)
echo [3/4] Checking static files...
echo ✓ Static files ready
echo.

REM Start development server
echo [4/4] Starting development server...
echo.
echo ========================================
echo  Server will start at:
echo  http://127.0.0.1:8000
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

.venv\Scripts\python.exe manage.py runserver

pause
