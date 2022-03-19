@ECHO OFF
:: This batch file compiles MessyFolderOrganizer application
:: The generated app is in the ./dist folder
:: First make sure to "pip install -r requirements.txt"
TITLE Compiling MessyFolderOrganizer...
MKDIR dist\resources\graphics
MKDIR dist\resources\configs
ROBOCOPY "..\resources\graphics" "dist\resources\graphics" /mir
ROBOCOPY "..\resources\configs" "dist\resources\configs" extensions.json /mt /z
ROBOCOPY "..\resources\configs" "dist\resources\configs" log_config.ini /mt /z
pyinstaller --onefile -w compile.spec
ECHO:
ECHO DONE! PRESS ANYTHING TO OPEN OUTPUT FOLDER
ECHO:
PAUSE
START dist
