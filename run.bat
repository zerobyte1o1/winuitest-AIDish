@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result
allure generate ./result/
@REM serve ./result/ -p 8765
allure open ./allure-report/ -p 8765