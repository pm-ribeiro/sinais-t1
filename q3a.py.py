
# coding: utf-8

# In[131]:


#essas libs sao necessarias pra fazer os graficos e tals
import numpy as np
import matplotlib.pyplot as plt

#função degrau pra ex
def u_(t):
    if t>0:
        return 1
    else:
        return 0


# In[132]:


#o range dos vetores
t = np.arange(-3, 2, 0.01) 
u = np.vectorize(u_) #isso aqui tem q usar a jordana nao lembra pq, mas tem que :b

#original
xa = np.exp(-t)*u(t) - np.exp(-t)*u(t-1)

plt.subplot(221)
plt.plot(t, xa) #plotando o grafico
plt.title('Original')

#invertida
xb = np.exp(t)*u(-t) - np.exp(t)*u(-t-1)
plt.subplot(222)
plt.plot(t, xb) #plotando o grafico
plt.title('invertida')


#invertida e deslocada
t = np.arange(-4, 0, 0.01) 
xc = np.exp(t)*u(-t-2.03) - np.exp(t)*u(-t-1-2.03)
plt.subplot(223)
plt.plot(t, xc) #plotando o grafico
plt.title('invertida e deslocada')


plt.show()

