from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10,0.1)
y = x*0.2
y2 = np.sin(x)

#2개의 식이나 시리즈의 값을 동시에 보여주면서 비교
#범례 레전드를 통해 보여준다.
#범례의 위치를 정해준다.

plt.plot(x,y,'b',label='first')
plt.plot(x,y2,'r',label='second')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('matplotlib sample')
plt.legend(loc='upper right')
plt.show()

# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html

