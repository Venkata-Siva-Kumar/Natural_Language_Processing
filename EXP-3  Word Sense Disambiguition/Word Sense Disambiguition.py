#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[55]:


train = {
    "furniture" : ["put","coat","back","chair","sat","down","chair","made","timber","company","type","different","chair","award","fun","use"],
    "position" : [ "chair","institute","best","award","it","chair"]
}


# In[56]:


furniture = 3
position = 2
total = furniture+position

pw_fur = furniture/total
pw_pos = position/total
print(pw_fur,pw_pos)


# In[57]:


l = []
for item in train.values():
    l.extend(item)
print(l)


# In[58]:


vocabulary = len(set(l))
print("Size of Vocabulary : ",vocabulary)


# In[59]:


test = ["award","chair","it","company"]


# In[60]:


def find_count(word,sense):
    return train[sense].count(word)


# In[61]:


d1 = {}
d2 = {}
for word in test:
    fur = find_count(word,"furniture")
    print(word,fur)
    pos = find_count(word,"position")
    d1[word] = (fur+1) / (furniture+vocabulary)
    d2[word] = (pos+1) / (position+vocabulary)


# In[62]:


print(d1)
print(d2)


# In[67]:


import math
fur_score = 0
for val in d1.values():
    fur_score += math.log(val) / math.log(2)
fur_score += math.log(pw_fur) /math.log(2)
print(fur_score)


# In[77]:


pos_score = 0
for val in d2.values():
    pos_score += math.log(val) / math.log(2)
pos_score += math.log(pw_pos) / math.log(2)
print(pos_score)

