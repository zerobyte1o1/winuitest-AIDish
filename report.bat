set /p version=<c:/dish.listen
allure-combine --auto-create-folders c:/winuitest-AIDish/result/allure-report --dest c:/allure-html/%version%

timeout /t 5 > nul
start "" allure-combine c:/winuitest-AIDish/result/allure-report --dest c:/allure-html/%version%