@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp

start /B /WAIT allure generate --clean ./result/temp -o ./result/allure-report



set /p version=<c:/dish.listen

start /B allure-combine --auto-create-folders c:/winuitest-AIDish/result/allure-report --dest c:/allure-html/AIDIsh/%version%
