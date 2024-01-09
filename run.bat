@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt
netstat -ano | findstr :8765
if %errorlevel% equ 0 (
    echo Port 8765 is in use. Stopping the process using that port...
    FOR /F "tokens=5" %%P IN ('netstat -ano ^| findstr :8765') DO TaskKill.exe /F /PID %%P
)

set "command=pytest testCase/ --alluredir=./result"

echo Running command: !command!
!command!
@REM
@REM
@REM
@REM
@REM set "command=allure generate ./result -o ./result/report/"
@REM
@REM echo Running command: !command!
@REM !command!

set "command=allure serve ./result/ -p 8765 &"
echo Running command: !command!
!command!
