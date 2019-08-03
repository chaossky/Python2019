#일단 넘파이 라이브러리를 임포트한다.
import numpy as np
import matplotlib.pyplot as plt

#x의 범위는 0에서 10 까지 
x=np.arange(-5,5,0.1)
y=np.sin(x)
y2=np.cos(x)

plt.plot(x,y, label='sine')
plt.plot(x,y2, label='cosine')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Sin and Cosine Graph')
plt.legend()


plt.show()
