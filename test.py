import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,1000,num=10000)

x = np.cos(t/10)+100
y = 2*t

plt.figure(figsize=(5,5))
plt.plot(x,y,'r.')
plt.show()