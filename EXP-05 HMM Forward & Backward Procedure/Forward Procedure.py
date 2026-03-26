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


def forward(states,obs_seq,pi,trans,emiss):
    N = len(states)
    T = len(obs_seq)
    alpha = np.zeros((N,T))
    
    for i, state in enumerate(states):
        alpha[i, 0] = pi[state] * emiss[state][obs_seq[0]]
        
    for t in range(1, T):
        for i, state_i in enumerate(states):
            sum_prev = 0
            for j, state_j in enumerate(states):
                sum_prev += alpha[j, t-1] * trans[state_j][state_i]
                alpha[i, t] = sum_prev * emiss[state_i][obs_seq[t]]
    prob = alpha[0,T-1]+alpha[1,T-1]
    return alpha, prob


# In[4]:


alpha, prob = forward(states,obs_seq, pi, trans,emiss)
print("Alpha matrix:\n", alpha)


# In[5]:


print("Probability of observation sequence:", round(prob,4))


# In[ ]:




