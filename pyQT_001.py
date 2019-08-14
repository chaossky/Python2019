# -*- coding: utf-8 -*-
#필요한 모듈을 로드 한다.
"""
필요한 부분들을 불러옵니다. 
기본적인 UI 구성요소를 제공하는 위젯(클래스)들은
 PyQt5.QtWidgets 모듈에 포함되어 있습니다. 
 QtWidgets 모듈에 포함된 모든 클래스들과 
 이에 대한 자세한 설명은 QtWidgets 공식 문서에서
확인할 수 있습니다. 
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
#여기서 self는  MyApp객체를 말합니다.


    def initUI(self):
        
        self.setWindowTitle('My First Application')#타이틀 바에 나오는 창의 제목 설정
        self.move(300, 300) # 스크린 300,300의 위치로 이동
        self.resize(400, 200) # 위젯의 크기
        self.show()#보여주기


if __name__ == '__main__':# 혀재 모듈의 이름이 저장되는 내장변수

    app = QApplication(sys.argv)#모든 PyQT 어플리 케시션은 어플리케이션 객체를 생성해야 한다.
    ex = MyApp()
    sys.exit(app.exec_())