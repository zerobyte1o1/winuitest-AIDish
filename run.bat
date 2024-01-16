@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/
allure generate -c -o ./allure-report/ ./result
allure serve ./result/ -p 8765
