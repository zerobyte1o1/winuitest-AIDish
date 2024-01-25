@echo off

setlocal enabledelayedexpansion
set /p version=<c:/dish.listen
pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp
allure generate --clean ./result/temp -o ./result/allure-report

start "" allure-combine --auto-create-folders ./result/allure-report --dest c:/allure-html/%version%



