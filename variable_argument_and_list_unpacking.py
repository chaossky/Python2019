#가변인수 리스트 언팩킹을 사용

def print_numbers(*args):
    for arg in args:
        print(arg)


#가변인수(즉 인수의 갯수가 여러개인데 정해 지지 않고 함수를 정의)
#그리고 for문을 이용하여 그 인수 값을 출력하도록 함수를 정의 하였다.

print_numbers(10)

print_numbers(20,30,40)

x=[1,2,3,4]

print_numbers(*x)
