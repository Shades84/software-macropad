pyinstaller --name software-macropad_server --icon .\assets\swmp.ico --add-data server_config.ini;. --add-data assets/swmp.ico;assets --add-data README.MD;. .\app_server.py
pause