#결과창에서 한글이 깨짐을 방지하는 코드
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#######

#object 클래스 모든 클래스의 부모클래스
#__new__(), __init__(), __str__(), __eq__() 란 특수 메소드

class UndefinedVehicle(Exception):
    def __str__(self):
        return "정의되지 않은 탈것입니다."

vehicle=input("자전거, 오토바이, 자동차 중 하나를 고르세요.")

try:
    if vehicle not in ['자전거','오토바이','자동차']:
        raise UndefinedVehicle
except UndefinedVehicle as e:
    print(e)

