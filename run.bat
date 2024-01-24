@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
python run.py
@REM allure serve ./result/ -p 8765

