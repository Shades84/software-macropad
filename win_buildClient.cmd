pyinstaller -w --name software-macropad_client --icon .\assets\swmp.ico --add-data client_config.ini;. --add-data assets/swmp.ico;assets --add-data README.MD;. .\app_client.py
pause