@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp

start /B allure generate --clean ./result/temp -o ./result/allure-report


set /p version=<c:/dish.listen
@REM start /B allure-combine --auto-create-folders ./result/allure-report --dest c:/allure-html/%version%

start /B allure-combine --auto-create-folders ./result/allure-report --dest ./result/res