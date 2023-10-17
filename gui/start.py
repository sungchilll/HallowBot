import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from mask import maskWindow
from jicapp import jicappWindow
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("start.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class startWindow(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.startFunction)
        self.pushButton_2.clicked.connect(self.start2Function)

        

    def startFunction(self):
        self.hide()
        self.mask = maskWindow()
        # self.mask.exec()
        self.mask.show()

    def start2Function(self):
        self.hide()
        self.jicapp = jicappWindow()
        # self.mask.exec()
        self.jicapp.show()
        
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = startWindow() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
