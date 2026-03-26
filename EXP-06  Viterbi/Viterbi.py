#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import math


# In[7]:


states  = ['S1','S2','S3']
obs_seq = ['B','A','B']
pi      = {'S1':1,'S2':0,'S3':0}
trans   = {
            'S1':{'S1':0.8,'S2':0.2,'S3':0},
            'S2':{'S1':0,'S2':0.2,'S3':0.8},
            'S3':{'S1':0,'S2':0,'S3':1}
          }
emiss   = {
            'S1':{'A':0.6,'B':0.2,'C':0.2},
            'S2':{'A':0.1,'B':0.1,'C':0.8},
            'S3':{'A':0.5,'B':0.2,'C':0.3}
          }


# In[46]:


def viterbi(states,obs_seq,pi,trans,emiss):
    N = len(states)
    T = len(obs_seq)
    alpha = np.zeros((N,T))
    E = np.zeros((N, T-1), dtype=int)
    
    for i, state in enumerate(states):
        alpha[i, 0] = pi[state] * emiss[state][obs_seq[0]]
        
    for t in range(1, T):
        for i, state_i in enumerate(states):
            probs = []
            for j, state_j in enumerate(states):
                probs.append(alpha[j, t-1] * trans[state_j][state_i])
            best_prev = np.argmax(probs)
            alpha[i, t] = probs[best_prev] * emiss[state_i][obs_seq[t]]
            E[i, t-1] = best_prev
            
    S_opt = [0] * T               
    S_opt[T-1] = np.argmax(alpha[:, -1])

    for t in range(T-2, -1, -1):
        S_opt[t] = E[S_opt[t+1], t]

    state_path = [states[i] for i in S_opt]
    return alpha,state_path,E


# In[47]:


alpha,state_path,E = viterbi(states,obs_seq, pi, trans,emiss)


# In[49]:


print("Alpha matrix:\n", alpha)
print("Optimal state sequence:", state_path)
print("Backtracking Matrix:\n", E)
print("Maximum probability:", round(np.max(alpha[:, -1]),6))


# In[ ]:




