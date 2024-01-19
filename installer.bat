@echo off
title Fractal Generator Installer
echo Installing requirements for the fractal generator... make sure Python is downloaded and up to date and you checked "Add Python.exe to PATH" before installing!

python.exe -m pip install -q --upgrade pip

pip install -q tkinter Image ImageDraw

echo Requirements installed! If fractal_generator.py crashes, manually run "pip install tkinter Image ImageDraw"
pause