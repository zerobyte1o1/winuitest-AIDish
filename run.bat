@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
pytest testCase/ --alluredir=./result
set "command=allure serve --no-open ./result/ -p 8765 --no-open"
echo Running command: !command!
!command!
