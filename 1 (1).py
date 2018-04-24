import numpy as np
import matplotlib.pyplot as plt

def u_(t):
    if t>0:
        return 1
    else:
        return 0

t = np.arange(-13.0, 13.0, 1)
n = np.arange(-13.0, 13.0, 1)
u = np.vectorize(u_)

xa = (2+t)*u(t+2) + (8-2*t)*u(t-4) - (7-t)*u(t-7)
xb = 2*u(4-t) - 2*u(-1-t)
xc = (2*n**2)*u(n) - (n+50)*u(n-6) - (2*n**2-n-80)*u(n-9)
xd = (2*n**2)*u(-n) - (n+50)*u(-n-6) - (2*n**2-n-80)*u(-n-9)


plt.subplot(221)
plt.plot(t, xa)
plt.title('Questão 1 - letra a')

plt.subplot(222)
plt.step(t,xb)
plt.title('Questão 1 - letra b')

plt.subplot(223)
plt.stem(t,xc)
plt.title('Questão 1 - letra c')

plt.subplot(224)
plt.stem(t,xd)
plt.title('Questão 1 - letra d')

plt.show()
