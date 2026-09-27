@echo off
echo Starting AI Interview System Backend Server...
cd /d %~dp0
if exist backend\venv\Scripts\python.exe (
    backend\venv\Scripts\python.exe main.py
) else (
    python main.py
)
pause
