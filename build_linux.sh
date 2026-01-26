#!/bin/bash
# Build script for Linux
echo "Building Image Converter for Linux..."
pyinstaller --onefile --windowed --name "ImageConverter" --clean image_converter.py
echo "Done! Check dist/ImageConverter"
