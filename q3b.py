import numpy as np
import matplotlib.pyplot as plt

def u_(t):
    if t>=0:
        return 1
    else:
        return 0

u = np.vectorize(u_)

t = np.arange(-2, 2, 0.001)
x1 = t * u(t + 1) - t * u(t - 1)
plt.subplot(221)
plt.title('original')
plt.plot(t, x1)

t = np.arange(-2, 2, 0.001)
x2 = -(t * u(t + 1) - t * u(t - 1))
plt.subplot(222)
plt.title('refletido')
plt.plot(t, x2)

#deslocado 3 para esquerda
t = np.arange(-7, 0, 0.01)
x3 = (t+5)*u(t+6) - (t+5)*u(t+4)
plt.subplot(212)
plt.plot(t, x3)

#deslocado 2 pra direita
t = np.arange(-1, 7, 0.01)
xd2 = (t-1)*u(t) - (t-1)*u(t-2)
plt.plot(t, xd2)

#deslocado 0
t = np.arange(-2, 2, 0.001)
x0 = t * u(t + 1) - t * u(t - 1)
plt.plot(t, x0)

plt.title('Deslocado 3, 0, -2')


plt.show()
