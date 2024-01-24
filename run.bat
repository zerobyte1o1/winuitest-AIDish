@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp
allure generate ./result/temp -o ./result/allure-report
python run.py
@REM allure serve ./result/ -p 8765

