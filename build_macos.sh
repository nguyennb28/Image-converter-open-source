#!/bin/bash
# Build script for macOS
echo "Building Image Converter for macOS..."
pyinstaller --onefile --windowed --name "Image Converter" --clean image_converter.py
echo "Done! Check dist/Image Converter.app"
