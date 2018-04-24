import numpy as np
import matplotlib.pyplot as plt

def u_(t):
    if t>=0:
        return 1
    else:
        return 0

u = np.vectorize(u_)
t = np.arange(-7,10, 1)
x1 = u(t) + 2*u(t-3) - 2*u(t-6) - u(t-6)
plt.subplot(221)
plt.stem(t,x1)

x2 = 3*u(t+2) - u(t-1) - u(t-2) - u(t-3)
plt.subplot(222)
plt.stem(t,x2)

x = np.convolve(x1,x2,'same')
plt.subplot(212)
plt.title('Questão 6')
plt.stem(t,x)

plt.show()
