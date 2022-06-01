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
pyinstaller -w --onefile ..\main.py --icon app.ico --name Messy-Folder-Organizer --splash splashfile.png
ECHO:
ECHO DONE! PRESS ANYTHING TO OPEN OUTPUT FOLDER
ECHO:
PAUSE
START dist
