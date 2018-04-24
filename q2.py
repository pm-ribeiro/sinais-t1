import numpy as np
import matplotlib.pyplot as plt

def u_(t):
    if t>=0:
        return 1
    else:
        return 0

t = np.arange(-6.0, 8.0, 0.01)
u = np.vectorize(u_)

xa = ((3 + t) * u(t + 3)) - ((2 + t) * u(t + 2)) - ((t + 1) * u(t + 1)) + ((t - 1) * u(t - 1)) + ((2*t - 4) * u(t - 2)) + ((-t*2 + 8) * u(t - 4))



plt.subplot(221)

plt.ylabel('x(t)')
plt.xlabel('t')
plt.plot(t,xa)
plt.title('2 a)')

t = np.arange(-6.0, 9.0, 1)
xb = (2*t)*u(t+3) - (2*(t-3))*u(t-3)
plt.subplot(222)
plt.ylabel('y[n]')
plt.xlabel('n')
plt.stem(t, xb)
plt.title('2 b)')

plt.show()