
# coding: utf-8

# In[27]:


def flatten(aList):
    if aList == []:
        return aList
    if isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])


# In[25]:


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


# In[37]:


flatten(aList)

