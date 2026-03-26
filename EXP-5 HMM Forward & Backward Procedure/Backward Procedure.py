#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math


# In[2]:


states  = ['S1','S2']
obs_seq = ['W3','W2','W3']
pi      = {'S1':1,'S2':0}
trans   = {
            'S1':{'S1':0.6,'S2':0.4},
            'S2':{'S1':0.7,'S2':0.3}
          }
emiss   = {
            'S1':{'W3':0.5,'W2':0.5},
            'S2':{'W3':0.2,'W2':0.8}
          }


# In[3]:


def backward(states,obs_seq,pi,trans,emiss):
    T = len(obs_seq)
    N = len(states)

    beta = np.zeros((N, T))

    beta[0,T-1] = 1.0
    beta[1,T-1] = 1.0
    
    for t in range(T-2, -1, -1):
        for i, state_i in enumerate(states):
            total = 0.0
            for j, state_j in enumerate(states):
                total += ( trans[state_i][state_j] * emiss[state_j][obs_seq[t+1]] * beta[j,t+1] )
            beta[i,t] = total
    
    prob = 0
    for i, state_i in enumerate(states):
        prob += ( pi[state_i] * beta[i, 0] * emiss[state_i][obs_seq[0]] )
    return beta, prob


# In[4]:


beta, prob = backward( states, obs_seq, pi, trans, emiss )
print("Beta matrix:\n",beta)


# In[5]:


print("Final Probability:", prob)


# In[ ]:




