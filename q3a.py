
# coding: utf-8

# In[6]:


#essas libs sao necessarias pra fazer os graficos e tals
import numpy as np
import matplotlib.pyplot as plt

#função degrau pra ex
def u_(t):
    if t>0:
        return 1
    else:
        return 0


# In[7]:


#o range dos vetores
t = np.arange(-1, 2, 0.01) 
u = np.vectorize(u_) #isso aqui tem q usar a jordana nao lembra pq, mas tem que :b

#original
xa = np.exp(-t)*u(t) - np.exp(-t)*u(t-1)

plt.subplot(221)
plt.plot(t, xa) #plotando o grafico
plt.title('Original')

#invertida
t = np.arange(-2, 1, 0.01) 
xb = np.exp(t)*u(-t) - np.exp(t)*u(-t-1)
plt.subplot(222)
plt.plot(t, xb) #plotando o grafico
plt.title('invertida')




# In[76]:


#deslocada -2
t = np.arange(1, 4, 0.01) 
xc = (np.exp(-t)*u(t-2) - np.exp(-t)*u(t-1-2))*7.5
plt.subplot(223)
plt.plot(t, xc) #plotando o grafico
plt.title('deslocada -2')


# In[54]:
#original
t = np.arange(-1, 2, 0.01) 
xz = np.exp(-t)*u(t) - np.exp(-t)*u(t-1)
plt.plot(t, xz) #plotando o grafico
plt.title('Original')

#deslocada 3
t = np.arange(-4, -1, 0.01) 
xd = (np.exp(-t)*u(t+3) - np.exp(-t)*u(t-1+3))*0.05
#plt.subplot(224)
plt.plot(t, xd) #plotando o grafico
plt.title('deslocada +3, 0, -2')


plt.show()

