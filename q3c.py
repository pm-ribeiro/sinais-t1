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



t = np.arange(-5.0, 10, 0.01)

#deslocada 0
xc = u(t-1) + 1*u(t-3) - 2*u(t-4)

#deslocada 3
xd = u(t-1+3) + 1*u(t-3+3) - 2*u(t-4+3)

#deslocada -2
xe = u(t-1-2) + 1*u(t-3-2) - 2*u(t-4-2)
plt.subplot(212)
plt.title('deslocada 3,0, -2')
plt.step(t,xc)
plt.step(t,xd)
plt.step(t,xe)

plt.show()
