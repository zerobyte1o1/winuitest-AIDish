@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=c:/result
@REM allure serve ./result/ -p 8765

