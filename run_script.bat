@echo off
for /l %%x in (1, 1, 7) do (
    "C:\Users\User\.conda\envs\scraper\python.exe" "c:\Users\User\OneDrive - Universidade de Aveiro\Desktop\UA\Tese\TwitterScraping\scrap_the_twitter.py"
    timeout /t 900 /nobreak
)
pause