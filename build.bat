@echo off
cd /d %~dp0
.venv\Scripts\pyinstaller --noconfirm --windowed --onefile --add-data="web:web" main.py