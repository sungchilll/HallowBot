import sys
import subprocess
from PyQt5 import uic
from PyQt5.QtWidgets import *
from question import questWindow
from origin import originWindow


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("app.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn1.clicked.connect(self.btn1Func)
        self.btn2.clicked.connect(self.btn2Func)
        self.btn3.clicked.connect(self.btn3Func)
        self.btn4.clicked.connect(self.btn4Func)
        self.btn5.clicked.connect(self.btn5Func)
        self.btn6.clicked.connect(self.btn6Func)
        self.question_btn.clicked.connect(self.queFunction)
        self.question_btn_2.clicked.connect(self.goFirst)
        
        
    def btn1Func(self):        
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 3.0, y: 0.501}, orientation:{w: 1.0}}}}'", shell=True)
        self.hide()
        self.origin = originWindow()
        #self.question.exec()
        self.origin.show()
            
        
    def btn2Func(self):
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 5.0, y: 0.501}, orientation:{w: 1.0}}}}'", shell=True)
        self.hide()
        self.origin = originWindow()
        #self.question.exec()
        self.origin.show()
        
    def btn3Func(self):
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 7.0, y: 0.501}, orientation:{w: 1.0}}}}'", shell=True)
        self.hide()
        self.origin = originWindow()
        #self.question.exec()
        self.origin.show()

    def btn4Func(self):
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 9.0, y: 0.501}, orientation:{w: 1.0}}}}'", shell=True)
        self.hide()
        self.origin = originWindow()
        #self.question.exec()
        self.origin.show()

    def btn5Func(self):
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 11.0, y: 0.501}, orientation:{w: 1.0}}}}'", shell=True)
        self.hide()
        self.origin = originWindow()
        #self.question.exec()
        self.origin.show()
    
    def btn6Func(self):
        subprocess.run("export TURTLEBOT3_MODEL=waffle", shell=True)
        subprocess.run("ros2 action send_goal navigate_to_pose nav2_msgs/action/NavigateToPose '{pose: {pose: {position: {x: 13.0, y: 0.501}, orientation:{w: 1.0}}}}'", shell=True)
        self.hide()
        self.origin = originWindow()
        #self.question.exec()
        
        self.origin.show()
    
    def queFunction(self):
        # self.hide()
        self.question = questWindow()
        #self.question.exec()
        self.question.show()
        

    def goFirst(self):
        # self.hide()
        # subprocess.run("cd pyqt", shell=True)
        self.close()
        subprocess.run("python3 start.py", shell=True)
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
