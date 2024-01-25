@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp
start "" allure generate --clean ./result/temp -o ./result/allure-report
set /p version=<c:/dish.listen
allure-combine --auto-create-folders ./result/allure-report --dest c:/allure-html/%version%



