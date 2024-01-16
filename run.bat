@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result/allure-xml
allure generate -o ./allure-report/  ./result
allure open ./allure-report
