<<<<<<< HEAD
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10)
y1 = x*5
y2 = x**2

plt.subplot(2,1,1)
plt.plot(x,y1)
plt.subplot(2,1,2)
plt.plot(x,y2)
=======
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10)
y1 = x*5
y2 = x**2

plt.subplot(2,1,1)
plt.plot(x,y1)
plt.subplot(2,1,2)
plt.plot(x,y2)
>>>>>>> 18c0589cd863ddd50038bf9d112beb00982f3dfd
plt.show()