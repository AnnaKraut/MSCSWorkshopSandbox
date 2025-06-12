import numpy as np
import matplotlib.pyplot as plt

print("Hello World")

x = np.linspace(0,10,100)

y = np.exp(x)

plt.plot(x,y)
plt.show()