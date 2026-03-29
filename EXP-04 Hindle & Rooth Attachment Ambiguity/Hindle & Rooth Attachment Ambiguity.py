#!/usr/bin/env python
# coding: utf-8

# In[11]:


import math
from nltk.tokenize import word_tokenize
from nltk import bigrams


# In[12]:


with open("file.txt",'r') as f:
    corpus = f.read()
print(corpus)


# In[13]:


tokens = word_tokenize(corpus.lower())


# In[14]:


print(tokens)


# In[15]:


elem_count = {}
for element in tokens:
    elem_count[element] = elem_count.get(element,0)+1


# In[16]:


print(elem_count)


# In[17]:


bi_grams = list(bigrams(tokens))


# In[18]:


bigram_count = {}
for bigram in bi_grams:
    bigram_count[bigram] = bigram_count.get(bigram,0)+1
print(bigram_count)


# In[19]:


noun = input("Enter the Noun : ")
verb = input("Enter the Verb : ")
prep = input("Enter the Preposition : ")


# In[20]:


n = elem_count.get(noun,0)
v = elem_count.get(verb,0)
p_n =bigram_count.get((noun,prep),0)
p_v =bigram_count.get((verb,prep),0)
n,v,p_n,p_v


# In[21]:


def cal_prob(p_v,p_n,v,n):
    prob_v = p_v/v if v>0 else 0
    prob_n = p_n/n if n>0 else 0
    return prob_v,prob_n


# In[22]:


prob_v,prob_n = cal_prob(p_v,p_n,v,n)


# In[23]:


def cal_lam(prob_v,prob_n):
    lamb = math.log((prob_v*(1-prob_n))/prob_n , 2)
    return lamb


# In[24]:


lamda = cal_lam(prob_v,prob_n)
lamda


# In[25]:


if lamda >0:
    print("The Preposition is attached with Verb")
elif lamda<0:
    print("The Preposition is attached with Noun")
else:
    print("The Preposition attached cannot be determined")


# In[ ]:




