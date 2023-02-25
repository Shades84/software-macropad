# https://www.youtube.com/watch?v=li7esLMuFhE
# https://www.pythonguis.com/pyqt5/
# https://build-system.fman.io/pyqt5-tutorial
# https://github.com/altendky/pyqt-tools/issues/98#issuecomment-968296553
# https://realpython.com/qt-designer-python/


import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from main_macropad import Ui_MainWindow
from configparser import ConfigParser

from pynput.keyboard import Key, Controller
import pywinctl as pwc

from qt_material import apply_stylesheet

config_object = ConfigParser()
config_object.read("config.ini")
#windowTitles = pwc.getWindowsWithTitle('0 A.D.')
#appWindow = windowTitles[0]

def run_button(button_name):
    try:
        subprocess.run(button_name)
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Couldn't execute requested command. Please revise chosen action's code.")
        msg.exec_()

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        # window stuff
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle('alpha-0.0.2')
        # self.keyboard = Controller()
        
        
        # setup buttons
        self.buttonGridSetup()
        # self.verticalSlider_4.valueChanged.connect(self.onSliderChanged)
        
        # clock timer
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

    
    # def onSliderChanged(self, value):
        # param = 'https://www.google.com/search?q=' + str(value)
        # subprocess.run(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',param])
        
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
        button00CMD = button00config["cmd"].split(",")
        run_button(button00CMD)


    def onButton01Clicked(self):
        button01config = config_object["button01"]
        button01CMD = button01config["cmd"].split(",")
        run_button(button01CMD)

    def onButton02Clicked(self):
        button02config = config_object["button02"]

        button02CMD = button02config["cmd"].split(",")
        run_button(button02CMD)
        
        # testing some pynput stuff here. Nothing to see.

        # button02Key = button02config["key"]
        # kc=keyboard.KeyCode.from_char('cmd')
        # print(kc)
        # print(type(kc))
        # print(kc.char)
        # print(type(Key.cmd))
        # print(button02Key)
        # self.keyboard.press(Key.cmd)
        # self.keyboard.press('1')
        # self.keyboard.release('1') 
        # self.keyboard.release(Key.cmd)


    def onButton10Clicked(self):
        button10config = config_object["button10"]
        button10CMD = button10config["cmd"].split(",")
        run_button(button10CMD)

    def onButton11Clicked(self):
        button11config = config_object["button11"]
        button11CMD = button11config["cmd"].split(",")
        run_button(button11CMD)

    def onButton12Clicked(self):
        button12config = config_object["button12"]
        button12CMD = button12config["cmd"].split(",")
        run_button(button12CMD)
    
    def onButton20Clicked(self):
        button20config = config_object["button20"]
        button20CMD = button20config["cmd"].split(",")
        run_button(button20CMD)
    
    def onButton212Clicked(self):
        button212config = config_object["button212"]
        button212CMD = button212config["cmd"].split(",")
        run_button(button212CMD)


def main():
    app = QApplication(sys.argv)
    appConfig = config_object["appConfig"]
    apply_stylesheet(app, theme=appConfig["theme"])

    win = Window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()