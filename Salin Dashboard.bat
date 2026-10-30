@echo off
rem Salin dashboard ke clipboard untuk ditempel ke chat mentor (bila mentor tidak bisa membuka GitHub).
chcp 65001 >nul
title Salin Dashboard - Dapur Data
cd /d "%~dp0"
where python >nul 2>nul
if %errorlevel%==0 (python tools\salin_dashboard.py %*) else (py tools\salin_dashboard.py %*)
echo.
pause
