import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from app import WindowClass
import time
#from thermotest import *
import cv2
from question import questWindow

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("hightemp.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class hightempWindow(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        
        self.pushButton_2.clicked.connect(self.thermo)

    def thermo(self):

        #threadThermalCam = camThread("thermal camera", "/dev/video2", cv2.VideoWriter.fourcc('Y','1','6',' '))
        #threadThermalCam.start()
        # self.hide()
        self.question = questWindow()
        #self.question.exec()
        self.question.show()
        # if dan == 0:
        time.sleep(3)
        
        
        self.hide()
        self.app = WindowClass()
        #self.question.exec()
        self.app.show()
 
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = hightempWindow() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
