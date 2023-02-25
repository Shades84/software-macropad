import asyncio
import subprocess
from websockets import serve
from configparser import ConfigParser   

async def main():
    async with serve(cmdHandler, uri, port):
        print('websocket started')
        await asyncio.Future()  
    
async def cmdHandler(websocket):
    async for message in websocket:
        command = message.split(",")
        print("received " + str(message))
        run_button(command)

def run_button(button_cmd):
    try:
        subprocess.run(button_cmd)
    except:
        print("error")

config_object = ConfigParser()
config_object.read("server_config.ini")
appConfig = config_object["appConfig"]
uri = appConfig["IP"]
port = int(appConfig["PORT"])
print("Hosting on " + uri + ":" + str(port))
asyncio.run(main())