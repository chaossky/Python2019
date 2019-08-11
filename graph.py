<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
def f(t):
    'A damped exponential'
    s1 = np.cos(40 * np.pi * t)
    e1 = np.exp(-t**2)
    return s1 * e1

t1 = np.arange(0.0, 5.0, .1)

l = plt.plot(t1, f(t1), 'ro')

plt.setp(l, markersize=10)
plt.setp(l, markerfacecolor='C0')
plt.show()
=======
import matplotlib.pyplot as plt
import numpy as np


def f(t):
    'A damped exponential'
    s1 = np.cos(3 * np.pi * t)
    e1 = np.exp(-t)
    return s1 * e1


t1 = np.arange(0.0, 5.0, .5)

l = plt.plot(t1, f(t1), 'ro')
plt.setp(l, markersize=20)
plt.setp(l, markerfacecolor='C0')

plt.show()
>>>>>>> 36a4b702351445ed74bb50572010fc5b2edd58ba
