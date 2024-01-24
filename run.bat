@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp
allure generate  ./result/temp -o ./result/allure-report
allure-combine --auto-create-folders ./result/allure-report --dest c:/allure-html/1212/
@REM allure serve ./result/ -p 8765

