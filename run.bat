@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt

set "command=pytest testCase/ --alluredir=./result --clean-alluredir"

echo Running command: !command!
!command!

set "command=allure generate ./result -c -o ./result/report/"

echo Running command: !command!
!command!

REM Check if port 8765 is in use and kill the process if necessary
set "command=netstat -ano | findstr :8765"

echo Running command: !command!
!command!

if %errorlevel% equ 0 (
    set "command=FOR /F "tokens=5" %%P IN ('netstat -ano ^| findstr :8765') DO (taskkill /F /PID %%P)"
    echo Running command: !command!
    !command!
)

set "command=allure serve ./result/ -p 8765"

echo Running command: !command!
!command!
