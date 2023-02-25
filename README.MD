# about
this is a 'macropad' i made to use with the steam deck, but it can be used for anything. Not tested, but i imagine it will work with any sort of touch screen connected to your computer.

I used the stylesheets from UN-GCPDS/qt-material found [here](https://github.com/UN-GCPDS/qt-material) so it actually looks nice


**CURRENTLY NEED HELP WITH SENDING KEYBOARD PRESSES TO SPECIFIC WINDOWS ON LINUX, ANY INPUT IS APPERCIATED** 
# how to run
## create virtual environment
first run\
```python -m venv venv ```
## activate virtual environment
*Windows*\
```venv/Scripts/activate.bat``` for regular command prompt  **or**\
```venv/Scripts/Activate.ps1``` for powershell

*Linux*\
```source venv/bin/activate```

## install requirements
```pip install -r requirements.txt```

## run app
```python app.py```


# how to build for distribution
from the root of the project dir, run:\
```pyinstaller -w --add-data 'config.ini;.' .\app.py```\
```pyinstaller -w --add-data 'client_config.ini;.' .\app_client.py```
```pyinstaller -w --add-data 'server_config.ini;.' .\app_server.py```

-w creates a windowed application (so it doesnt show the terminal)\
--add-data tells the program to copy the config.ini file to the end result folder\
.\app.py is the main app \

# customizing the app
## GUI layout
modify the .ui file in qt designer (or by hand if you're brave) \
run the command:\
```pyuic5 -o main_mainmacropad.py macropad_v0.1.ui```\
to convert changes to python code

## button labels and functions
changes to buttons can be made in the config.ini file. Commands are somewhat fussy about how they need to be formated

# to do
- more descriptive names for files/refactoring code
- add functionality to sliders and dials (any suggestions?)
- add themes selection to config file 
- try to implement sending keystrokes to games (maybe its an issue because it pulls focus from the game, unsure)
- swappable profiles
- server/client setup for multiple computers?

# helpful links and other projects
https://www.youtube.com/watch?v=li7esLMuFhE \
https://www.pythonguis.com/pyqt5/ \
https://build-system.fman.io/pyqt5-tutorial \
https://github.com/altendky/pyqt-tools/issues/98#issuecomment-968296553 \
https://realpython.com/qt-designer-python/ 
https://github.com/timothycrosley/streamdeck-ui
https://rodriguezanton.com/remote-sound-board-using-fastapi-vue-and/