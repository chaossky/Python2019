#이 프로그램은 두점이 주어지면 기울기를 구하고 1차 방정식을
# y=mx+b 형식으로 출력하도록 하는 것

#점의 좌표를 각각의 좌표로
x1=0
y1=4
x2=4
y2=5
if(x2!=x1):
    slope=(y2-y1)/(x2-x1)
else :
    slope=0
    
print(slope)
b=y2-slope*x2
c=y1-slope*x1
print(b)
print(c)

print("y =",slope,"* x + ",c)