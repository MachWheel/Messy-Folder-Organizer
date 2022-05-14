@ECHO OFF
TITLE Messy Folder Organizer Compiler
ECHO:
ECHO Messy Folder Organizer Compiler
ECHO:
ECHO This batch script compiles the application
ECHO:
ECHO Make sure to proper configure the project virutalenv first.
ECHO:
ECHO You should run this script inside the project virtualenv to avoid problems.
ECHO:
ECHO The generated app will be in the ./dist folder
ECHO:
PAUSE
MKDIR dist\resources\configs
ROBOCOPY "..\resources\configs" "dist\resources\configs" extensions.json /mt /z
ROBOCOPY "..\resources\configs" "dist\resources\configs" log_config.ini /mt /z
pyinstaller -w --onefile ..\main.py --icon app.ico --name Messy-Folder-Organizer
ECHO:
ECHO DONE! PRESS ANYTHING TO OPEN OUTPUT FOLDER
ECHO:
PAUSE
START dist
