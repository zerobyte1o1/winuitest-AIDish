@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/
allure generate -o -c ./allure-report/ ./result
allure serve ./result/ -p 8765
