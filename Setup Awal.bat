@echo off
rem Setup pertama kali: jalankan SEKALI setelah repo kosong dibuat di GitHub.
chcp 65001 >nul
title Setup Awal - Dapur Data
cd /d "%~dp0"
where python >nul 2>nul
if %errorlevel%==0 (python tools\setup_awal.py %*) else (py tools\setup_awal.py %*)
echo.
pause
