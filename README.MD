# about
this is a 'macropad' i made to use with the steam deck, but it can be used for anything. Not tested, but i imagine it will work with any sort of touch screen connected to your computer.

I used the stylesheets from UN-GCPDS/qt-material found [here](https://github.com/UN-GCPDS/qt-material) so it actually looks nice


**CURRENTLY NEED HELP WITH SENDING KEYBOARD PRESSES TO SPECIFIC WINDOWS ON LINUX, ANY INPUT IS APPERCIATED** 
# how to run
- grab the latest from the release page use ```software-macropad``` to run the macropad on the same device you want to control. Use the ```server``` and ```client``` to control one device from another on the same network
- edit the ```config.ini``` file to your prefference. See 
- run the executable

# \*new!* server/client
- configure the IP and port in ```server_config.ini``` and ```client_config.ini```. This will be the IP of the device you want to control. As for port, ive been using ```8765```
- run the server on the device you want to control
- run the client on the thing you want to be a macropad (such as steamdeck or touchscreen windows device)

# development
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
First, ensure your virtual environment is active.\
If you're on windows, you can run the corresponding ```win_buildXXX.cmd``` script. This handles all the command line things. Linux scripts comming soon.

If oyu want to run the build command yourself, from the root of the project dir, run:\
```pyinstaller -w -n software-macropad --add-data 'config.ini;.' .\app.py```\
```pyinstaller -w -n software-macropad_client --add-data 'client_config.ini;.' .\app_client.py```\
```pyinstaller -n software-macropad_server --add-data 'server_config.ini;.' .\app_server.py```

-w creates a windowed application (so it doesnt show the terminal) (remove this for linux)\
-n name to assign to bundled app\
--add-data tells the program to copy the config.ini file to the end result folder (change ; to : for linux)\
.\app.py is the main app (remove .\ part for linux)

# customizing the app
## GUI layout
modify the .ui file in qt designer (or by hand if you're brave) \
run the command:\
```pyuic5 -o main_mainmacropad.py macropad_v0.1.ui```\
to convert changes to python code
## GUI theme
change the ```theme``` in the ```appConfig``` section of ```config.ini```. Possible options are presented at the top of the file.
## button labels and functions
changes to buttons can be made in the config.ini file. Commands are somewhat fussy about how they need to be formated. Program is using the python ```subprocess.run()``` method. Write your commands to have the program you want to launch as the first item and any parameters after, seperated by commas. 
### example: steam games
```steam,steam://rungameid/APPID```\
where APPID is the app ID of the game or program. You can find your game's ID on https://steamdb.info/. Also works for non-steam shortcuts, but that is a little more complicated for finding the app ID. 

### example: launch website
this will vary from browser to browser but this is how it is for chrome\
```PATH/TO/WEBBROWSER.exe, -PARAM1, -PARAM2```

# troubleshooting
## button not working
- check that config.ini is setup correctly. Comma seperated launch options, be mindful with quotations
- **windows:** is your program in your PATH environment variable?
## can't connect between server and client
- work in progress

# to do
- build scripts for linux
- figure out how to kill server on linux (woops, didnt think of that)
- implement sending keystrokes to games (currently looking at pynput)
- add functionality to sliders and dials (any suggestions?)
- swappable profiles
- add logging
- icons on buttons?

# helpful links and other projects
https://www.youtube.com/watch?v=li7esLMuFhE \
https://www.pythonguis.com/pyqt5/ \
https://build-system.fman.io/pyqt5-tutorial \
https://github.com/altendky/pyqt-tools/issues/98#issuecomment-968296553 \
https://realpython.com/qt-designer-python/ 
https://github.com/timothycrosley/streamdeck-ui
https://rodriguezanton.com/remote-sound-board-using-fastapi-vue-and/