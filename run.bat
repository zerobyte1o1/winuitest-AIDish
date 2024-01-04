@echo off

pytest testCase/ --alluredir=./result --clean-alluredir

allure generate ./result -c -o ./result/report/

REM Check if port 8765 is in use and kill the process if necessary
netstat -ano | findstr :8765
if %errorlevel% equ 0 (
    FOR /F "tokens=5" %%P IN ('netstat -ano ^| findstr :8765') DO (
        taskkill /F /PID %%P
    )
)

allure serve ./result/ -p 8765