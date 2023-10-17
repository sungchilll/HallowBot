import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import time
import subprocess
from startmask import masks
from temp import tempWindow

#mask detection module
# def maskss():
# 	subprocess.run("cd /home/hallowbot/mask_detection", shell=True)
# 	subprocess.run("python3 startmask.py", shell=True)

# print(maskss())

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("nomask.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class nomaskWindow(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.mask_detecting)

    def next(self):
        self.hide()
        self.temp = tempWindow()
        # self.temp.exec()
        self.temp.show()

    def mask_detecting(self):
        
        result = masks()
        print(result)
        if(result ==2):
            # time.sleep(3000)
            # next()
            self.hide()
            self.temp = tempWindow()
            # self.temp.exec()
            self.temp.show()
        else:
            self.hide()
            self.nomask = nomaskWindow()
            # self.temp.exec()
            self.nomask.show()
            

    
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = nomaskWindow() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    

