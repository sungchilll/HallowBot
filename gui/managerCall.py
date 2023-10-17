import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from callorigin import calloriginWindow
import subprocess
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("managerCall.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class managerCallWindow(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.startFunction)

    def startFunction(self):
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 3.0, y: 0.501}, orientation:{w: 1.0}}}}'", shell=True)
        self.hide()
        self.callOrigin = callOriginWindow()
        #self.question.exec()
        self.callOrigin.show()
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = managerCallWindow() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
