@echo off
REM Database Setup Script

echo ========================================
echo  MySQL Database Setup
echo ========================================
echo.
echo This script will help you set up the MySQL database.
echo.
echo Please ensure MySQL server is running before continuing.
echo.
pause

echo.
echo Creating database and user...
echo.
echo Please enter your MySQL root password when prompted.
echo.

mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS quizdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; CREATE USER IF NOT EXISTS 'quizuser'@'localhost' IDENTIFIED BY 'quizpass'; GRANT ALL PRIVILEGES ON quizdb.* TO 'quizuser'@'localhost'; FLUSH PRIVILEGES;"

if errorlevel 1 (
    echo.
    echo ERROR: Database setup failed.
    echo Please check:
    echo  - MySQL server is running
    echo  - You entered the correct root password
    echo  - You have permission to create databases
    pause
    exit /b 1
)

echo.
echo ✓ Database 'quizdb' created successfully!
echo ✓ User 'quizuser' created with password 'quizpass'
echo ✓ Privileges granted
echo.
echo ========================================
echo  Next Steps:
echo ========================================
echo 1. Update .env file with your settings
echo 2. Run: .venv\Scripts\python.exe manage.py migrate
echo 3. Run: .venv\Scripts\python.exe manage.py createsuperuser
echo 4. Run: start.bat to start the server
echo.
pause
