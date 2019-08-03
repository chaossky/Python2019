from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10)
y1 = x*5
y2 = x**2

plt.subplot(2,1,1)
plt.plot(x,y1)
plt.subplot(2,1,2)
plt.plot(x,y2)
plt.show()