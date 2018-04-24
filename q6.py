import numpy as np
import matplotlib.pyplot as plt

def u_(t):
    if t>=0:
        return 1
    else:
        return 0

u = np.vectorize(u_)

#intervalo -7 a 9
n = np.arange(-7,9, 1)
x1 = u(n) + 2*u(n-3) - 2*u(n-6) - u(n-6)
plt.subplot(221)
plt.title('h[n]')
plt.stem(n,x1)


x2 = 3*u(n+2) - u(n-1) - u(n-2) - u(n-3)
plt.subplot(222)
plt.title('x[n]')
plt.stem(n,x2)

#x[n]*h[n-k]
x = np.convolve(x2,x1,'same')
plt.subplot(212)
plt.title('x[n]*h[n-k]')
plt.stem(n,x)

plt.show()
