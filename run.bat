@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result
allure generate ./result/xml -o allure-reports/
@REM serve ./result/ -p 8765
allure open ./allure-report/ -p 8765