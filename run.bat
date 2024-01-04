@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt

set "command=pytest testCase/ --alluredir=./result --clean-alluredir"

echo Running command: !command!
!command!

set "command=allure generate ./result -c -o ./result/report/ && allure serve ./result/ -p 8765"

echo Running command: !command!
!command!


