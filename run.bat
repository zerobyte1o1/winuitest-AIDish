@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt



set "command=pytest testCase/ --alluredir=./result"

echo Running command: !command!
!command!

ping 127.0.0.1 -n 5 >nul

netstat -ano | findstr :8765
if %errorlevel% equ 0 (
    echo Port 8765 is in use. Stopping the process using that port...
    FOR /F "tokens=5" %%P IN ('netstat -ano ^| findstr :8765') DO TaskKill.exe /F /PID %%P
)
set "command=allure generate ./result -o ./result/report/"

echo Running command: !command!
!command!

set "command=allure serve ./result/ -p 8765"
echo Running command: !command!
!command!

echo Executing the command: !command!
!command!

echo Running command: !command!
!command!
