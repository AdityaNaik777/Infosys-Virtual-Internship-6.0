# Project Setup Guide

## Prerequisites
- Python 3.13.7 (installed and configured)
- MySQL Server 8.0+ (running on localhost:3306)
- OpenAI API Key

## Installation Steps Completed ✅

### 1. Python Environment
- ✅ Virtual environment created at `.venv/`
- ✅ Python 3.13.7 configured

### 2. Dependencies Installed
All required packages have been installed:
- ✅ Django==5.2.8
- ✅ PyMySQL==1.1.1
- ✅ Pillow==10.4.0
- ✅ python-dotenv==1.0.1
- ✅ openai==1.47.0
- ✅ reportlab==4.2.5
- ✅ requests==2.32.3

### 3. Environment Variables
✅ `.env` file created with all necessary variables

## Next Steps (Manual Configuration Required)

### 1. Set Up MySQL Database
```sql
-- Login to MySQL as root
mysql -u root -p

-- Create database
CREATE DATABASE quizdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user and grant privileges
CREATE USER 'quizuser'@'localhost' IDENTIFIED BY 'quizpass';
GRANT ALL PRIVILEGES ON quizdb.* TO 'quizuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 2. Configure OpenAI API Key
Edit the `.env` file and replace `your-openai-api-key-here` with your actual OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Run Database Migrations
```powershell
.venv\Scripts\python.exe manage.py makemigrations
.venv\Scripts\python.exe manage.py migrate
```

### 4. Create Superuser
```powershell
.venv\Scripts\python.exe manage.py createsuperuser
```

### 5. Load Initial Data (Optional)
```powershell
.venv\Scripts\python.exe manage.py loaddata quizzes/fixtures/initial_data.json
```

### 6. Run Development Server
```powershell
.venv\Scripts\python.exe manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

## Project Structure

### Apps
- **accounts/** - User authentication and profile management
- **quizzes/** - Quiz generation, attempts, and performance tracking
- **core/** - Main project settings and configurations

### Key Features
- User registration and authentication
- AI-powered quiz generation using OpenAI GPT-3.5
- Performance tracking and analytics
- PDF report generation
- Leaderboard system
- AI-powered feedback

## Environment Variables Reference

| Variable | Description | Default/Example |
|----------|-------------|-----------------|
| SECRET_KEY | Django secret key | (generated) |
| DEBUG | Debug mode | True |
| DB_NAME | Database name | quizdb |
| DB_USER | Database user | quizuser |
| DB_PASSWORD | Database password | quizpass |
| DB_HOST | Database host | 127.0.0.1 |
| DB_PORT | Database port | 3306 |
| OPENAI_API_KEY | OpenAI API key | Required |
| ALLOWED_HOSTS | Allowed hosts | * |

## Troubleshooting

### MySQL Connection Issues
- Ensure MySQL server is running
- Verify database credentials in `.env`
- Check if PyMySQL is properly installed

### OpenAI API Issues
- Verify API key is valid
- Check API usage limits
- Ensure internet connectivity

### Media Files
- Media files are stored in `media/avatars/`
- Ensure proper permissions for file uploads

## Additional Commands

### Create new migrations
```powershell
.venv\Scripts\python.exe manage.py makemigrations
```

### Apply migrations
```powershell
.venv\Scripts\python.exe manage.py migrate
```

### Collect static files (for production)
```powershell
.venv\Scripts\python.exe manage.py collectstatic
```

### Run tests
```powershell
.venv\Scripts\python.exe manage.py test
```

### Django shell
```powershell
.venv\Scripts\python.exe manage.py shell
```
