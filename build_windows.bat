@echo off
REM Build script for Windows
echo Building Image Converter for Windows...
pyinstaller --onefile --windowed --name "Image Converter" --clean image_converter.py
echo Done! Check dist/Image Converter.exe
pause
