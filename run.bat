@echo off

setlocal enabledelayedexpansion
set /p version=<c:/dish.listen
pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp
set /p version=<c:/dish.listen

start /B allure generate --clean ./result/temp -o ./result/allure-report

timeout /t 3 >nul

start /SEPARATE allure-combine --auto-create-folders ./result/allure-report --dest c:/allure-html/%version%


