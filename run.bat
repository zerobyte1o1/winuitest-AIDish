@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/temp

call :generate_report
call :combine_report

exit /b

:generate_report
start "" allure generate --clean ./result/temp -o ./result/allure-report
exit /b

:combine_report
set /p version=<c:/dish.listen
start "" allure-combine --auto-create-folders ./result/allure-report --dest c:/allure-html/%version%
exit /b



