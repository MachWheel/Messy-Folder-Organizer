<p align="center"><img src="https://i.imgur.com/xQMVkec.png" alt="Messy Folder Organizer Logo"></p>
<h1 align="center">Messy Folder Organizer</h1>
<p align="center"><i>A quick and simple way to organize your messy folders.</i></p>

![MAIN_DEMO](https://s7.gifyu.com/images/MFO1.1.gif)


# How to use it
### Just open the app, choose a messy folder and start it!


# How it works
Messy Folder Organizer works by automatically categorizing and moving all the files inside a 
folder based on their extensions.

  - Just files are moved, not folders.

  - A log file is generated at the end to help visualizing which files were moved where.

It does that through a simple .json file located at **resources/configs/extensions.json**


# Shortcut: change supported extensions

![CONFIG_DEMO](https://s7.gifyu.com/images/ezgif.com-gif-maker27c95d2834741325.gif)


# How to install it
Just download the zip at *Releases*, extract and run the .exe file. No installation needed.


# Is it "portable"?
**Yes!** In other words, you need just **Messy-Folder-Organizer.exe** to run this app. 
To uninstall, just delete it.

  - However, the app generates local configuration files when executed.

    - If it's not needed to change supported extensions, you can delete all of those. 

    - Otherwise, you should keep those files together.


# Supported extensions
### [You can edit them if you want, see above.](https://github.com/WyllerMachado/Messy-Folder-Organizer#how-it-works)

### Documents
    .doc, .docx, .htm, .odt, .pdf, .xls, .xlsx, .xlsm, .ods, .ppt, .pptx, .txt, .mobi, .epub

### Pictures
    .ai, .bmp, .gif, .jpeg, .jpg, .png, .ps, .psd, .svg, .tif, .tiff

### Videos
    .3g2, .3gp, .avi, .flv, .h264, .m4v, .mkv, .mov, .mp4, .mpg, .mpeg, .rm, .swf, .vob, .wmv, .srt

### Audios
    .aif, .cda, .mid, .mp3, .mpa, .ogg, .wav, .wma, .wpl

### Programs
    .apk, .bat, .bin, .cgi, .pl, .com, .gadget, .jar, .msi, .wsf

### Compacted
    .7z, .arj, .deb, .pkg, .rar, .rpm, .tar.gz, .z, .zip, .iso

### Ignored
    .exe, .ico, .lnk, .py, .ini


# requirements.txt
    pyinstaller==5.0.1
    PySimpleGUI==4.59.0


# Cloning the repository:

First, open the command-line and check your Python version. This app was made using **Python 3.9**:

    py --version


Now, install virtualenv if you don't have it:
    
    py -m pip install virtualenv


Clone the repository and change the directory to it:
    
    git clone https://github.com/WyllerMachado/Messy-Folder-Organizer.git
    cd Messy-Folder-Organizer


Create a virtualenv for the project, then activate it:
    
    py -m venv venv
    .\venv\Scripts\activate


Install project dependencies:
    
    py -m pip install -r requirements.txt


Done. Now you can run the app typing:

    py main.py


# How to compile it:

### First: [clone the repository and properly configure its virtualenv (see above)](https://github.com/WyllerMachado/Messy-Folder-Organizer#cloning-the-repository)
### Second: change to the directory and activate virtualenv if it is not already activated.

    cd Messy-Folder-Organizer
    .\venv\Scripts\activate

## Easy way:

### Inside Messy-Folder-Organizer virtualenv, change the directory to compile and run the script:

    cd compile
    .\compile.bat

  - **The folder containing the generated .exe file will be opened automatically**

## Manual way:

Inside Messy-Folder-Organizer virtualenv, change the directory to compile folder and run pyinstaller:

    cd compile
    pyinstaller -w --onefile ..\main.py --icon app.ico --name Messy-Folder-Organizer
    
  - **The generated .exe file will be in .\compile\dist folder.**
