import numpy as np
import matplotlib.pyplot as plt

def u_(t):
    if t>=0:
        return 1
    else:
        return 0

u = np.vectorize(u_)
t = np.arange(-1.0, 5.0, 0.01)
xa = u(t-1) + 1*u(t-3) - 2*u(t-4)

plt.subplot(221)
plt.title('original')
plt.plot(t,xa)

t = np.arange(-6.0, 0.0, 0.01)
xb = u(-t-1) + 1*u(-t-3) - 2*u(-t-4)
plt.subplot(222)
plt.title('Invertida')
plt.plot(t,xb)

t = np.arange(-8.0, 0.0, 0.01)
xc = u(-t-1-2.03) + 1*u(-t-3-2.03) - 2*u(-t-4-2.03)
plt.subplot(212)
plt.title('Invertida e deslocada')
plt.step(t,xc)

plt.show()
