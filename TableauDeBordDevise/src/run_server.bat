@echo off
cd /d "C:\Users\dmard\Desktop\Study\La formation Python\TableauDeBordDevise"
call .venv\Scripts\activate
python src\manage.py runserver
pause