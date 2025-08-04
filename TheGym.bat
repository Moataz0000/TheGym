@echo off
REM ✅ الانتقال لمكان السكريبت
cd /d %~dp0

REM ✅ تفعيل البيئة الافتراضية
call .venv\Scripts\activate.bat

REM ✅ دخول مجلد config (لو manage.py فيه)
cd config

REM ✅ تشغيل السيرفر في الخلفية
start "" python manage.py runserver

REM ✅ الانتظار ثانيتين
timeout /t 2 >nul

REM ✅ فتح المتصفح Google Chrome على صفحة الأدمن
start chrome http://127.0.0.1:8000/admin/
