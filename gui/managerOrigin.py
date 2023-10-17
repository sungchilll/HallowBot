import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import subprocess
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("managerOrigin.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class managerOriginWindow(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.button.clicked.connect(self.btnF)

    def btnF(self):
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 0.000001, y: 0.000001}, orientation:{w: 1.0}}}}'", shell=True)
        self.close()
        subprocess.run("cd /home/hallow/pyqt1", shell=True)
        subprocess.run("python3 start.py", shell=True)
        
    	

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = managerOriginWindow() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
