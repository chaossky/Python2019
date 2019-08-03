import numpy as np
import matplotlib.pyplot as plt
 
N = 10000 # number of random walkers
T = 50  # time span
 
position = np.zeros((N, T+1))
 
for t in range(1, T+1):
    for i in range(N):
        position[i][t] = position[i][t-1] + np.random.normal()
 
plt.figure()
for i in range(N):
    plt.plot(position[i])
 
mean = np.mean(position, axis=0)
std = np.std(position, axis=0)
 
plt.figure()
plt.plot(mean)
plt.plot(std)
