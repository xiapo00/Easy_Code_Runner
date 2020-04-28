echo off
cls
pip install pyinstaller
pyinstaller -F C(Cpp)_Runner.py
pyinstaller -F Java_Runner.py
pyinstaller -F Python_Runner.py
mkdir exe
move dist\C(Cpp)_Runner.exe .\exe
move dist\Java_Runner.exe .\exe
move dist\Python_Runner.exe .\exe
rmdir /s/q build
rmdir /s/q dist
rmdir /s/q __pycache__
del C(Cpp)_Runner.spec
del Java_Runner.spec
del Python_Runner.spec
cls
echo finish
pause