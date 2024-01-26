@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp

start /B allure generate --clean ./result/temp -o ./result/allure-report
report.bat


