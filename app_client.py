# https://www.youtube.com/watch?v=li7esLMuFhE
# https://www.pythonguis.com/pyqt5/
# https://build-system.fman.io/pyqt5-tutorial
# https://github.com/altendky/pyqt-tools/issues/98#issuecomment-968296553
# https://realpython.com/qt-designer-python/


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from main_macropad import Ui_MainWindow
from configparser import ConfigParser
import asyncio
from websockets import connect

from qt_material import apply_stylesheet
from subprocess import call
config_object = ConfigParser()
config_object.read("client_config.ini")
appConfig = config_object["appConfig"]
SERVERURL = "ws://" + appConfig["IP"] + ":" + appConfig["PORT"] 

async def sendToServer(button_msg):
    async with connect(SERVERURL) as ws:
        await ws.send(button_msg)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        # window stuff
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle('alpha-0.0.2')
        
        # setup buttons
        self.buttonGridSetup()
        
        # clock timer
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Server uri set as " + SERVERURL)
        msg.exec_()
    def showTime(self):   
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm')
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.display(label_time)

    def buttonGridSetup(self):
        # row 0 (top)
        self.pushButton_00.setText(config_object["button00"]["text"])
        self.pushButton_00.clicked.connect(self.onButton00Clicked)

        self.pushButton_01.setText(config_object["button01"]["text"])
        self.pushButton_01.clicked.connect(self.onButton01Clicked)

        self.pushButton_02.setText(config_object["button02"]["text"])
        self.pushButton_02.clicked.connect(self.onButton02Clicked)

        # row 1 (middle)
        self.pushButton_10.setText(config_object["button10"]["text"])
        self.pushButton_10.clicked.connect(self.onButton10Clicked)

        self.pushButton_11.setText(config_object["button11"]["text"])
        self.pushButton_11.clicked.connect(self.onButton11Clicked)

        self.pushButton_12.setText(config_object["button12"]["text"])
        self.pushButton_12.clicked.connect(self.onButton12Clicked)

        # row 2 (bottom)
        self.pushButton_20.setText(config_object["button20"]["text"])
        self.pushButton_20.clicked.connect(self.onButton20Clicked)

        self.pushButton_212.setText(config_object["button212"]["text"])
        self.pushButton_212.clicked.connect(self.onButton212Clicked)


    def onButton00Clicked(self):
        button00config = config_object["button00"]
        button00cmd=button00config["cmd"]
        asyncio.run(sendToServer(button00cmd))

    def onButton01Clicked(self):
        button01config = config_object["button01"]
        button01cmd=button01config["cmd"]
        asyncio.run(sendToServer(button01cmd))

    def onButton02Clicked(self):
        button02config = config_object["button02"]
        button02cmd=button02config["cmd"]
        asyncio.run(sendToServer(button02cmd))

    def onButton10Clicked(self):
        button10config = config_object["button10"]
        button10cmd=button10config["cmd"]
        asyncio.run(sendToServer(button10cmd))

    def onButton11Clicked(self):
        button11config = config_object["button11"]
        button11cmd=button11config["cmd"]
        asyncio.run(sendToServer(button11cmd))

    def onButton12Clicked(self):
        button12config = config_object["button12"]
        button12cmd=button12config["cmd"]
        asyncio.run(sendToServer(button12cmd))
    
    def onButton20Clicked(self):
        button20config = config_object["button20"]
        button20cmd=button20config["cmd"]
        asyncio.run(sendToServer(button20cmd))
    
    def onButton212Clicked(self):
        button212config = config_object["button212"]
        button212cmd=button212config["cmd"]
        asyncio.run(sendToServer(button212cmd))

def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme=appConfig["theme"])
    print("Server uri set as " + SERVERURL)

    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
