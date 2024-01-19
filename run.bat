@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/
@REM allure serve ./result/ -p 8765

