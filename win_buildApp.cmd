pyinstaller -w --name software-macropad --icon .\assets\swmp.ico --add-data config.ini;. --add-data assets/swmp.ico;assets --add-data README.MD;. .\app.py
pause