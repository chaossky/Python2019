import numpy as np

np.random.seed(76923)

a = np.random.rand(2, 2)
b = np.random.randn(3, 3)
c = np.random.randint(1, 100, (4, 4), dtype=int)
d = np.random.randint(1, 50, (4, 4), dtype=int)
#난수를 정수로 1과10 사이에 4X4 크기의 배열을 형성
print("A matrix")
print(a)
print("B matrix")
print(b)

print("C matrix")
print(c)
print("D matrix")
print(d)

print("c*d matrix")
print(c*d)

print(c*d[0,3])