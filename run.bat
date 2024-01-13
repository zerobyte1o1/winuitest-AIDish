@echo off

setlocal enabledelayedexpansion

pip install -r requirements.txt

set "command=allure serve ./result/ -p 8765 --no-open"
echo Running command: !command!
!command!
