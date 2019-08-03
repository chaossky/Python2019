from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10)
y = x*5

#특정 부분만을 강조해서 보여 주기 위해
#범위를 정할 수 있다.
plt.xlim(2,4)
plt.ylim(5,40)

plt.plot(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('matplotlib sample')
plt.show()

