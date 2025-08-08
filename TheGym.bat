@echo off
REM Navigate to your Django project folder
cd dev\mycoffee

REM Activate the virtual environment
call .\venv\Scripts\activate

REM Open the browser at localhost
start http://localhost:8000

REM Run Django development server
python manage.py runserver

pause
