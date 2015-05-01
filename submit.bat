::python file.py %file_as_an_argument%
@echo off
set code=%~dp0submit.py
::echo %code% %1
python %code%  %1

