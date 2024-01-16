@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/
allure serve ./result/ -p 8765
allure generate -o ./allure-report/ ./result --clean

