import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("question.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class questWindow(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.yradi_1.clicked.connect(self.rdio1Function)
        self.nradi_1.clicked.connect(self.rdio1Function)

        self.yradi_2.clicked.connect(self.rdio2Function)
        self.nradi_2.clicked.connect(self.rdio2Function)
        
        self.yradi_3.clicked.connect(self.rdio3Function)
        self.nradi_3.clicked.connect(self.rdio3Function)

        self.submit_btn.clicked.connect(self.submitFunction)
        
    def rdio1Function(self):
        if self.yradi_1.isChecked():
            print("yes")
        elif self.nradi_1.isChecked():
            print("no")

    def rdio2Function(self):
        if self.yradi_2.isChecked():
            print("yes")
        elif self.nradi_2.isChecked():
            print("no")

    def rdio3Function(self):
        if self.yradi_3.isChecked():
            print("yes")
        elif self.nradi_3.isChecked():
            print("no")

    def submitFunction(self):
        #self.hide()
        self.close()
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = questWindow() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
