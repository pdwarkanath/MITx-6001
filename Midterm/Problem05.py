
# coding: utf-8

# In[6]:


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    result = 0
    for idx, elem in enumerate(listA):
        result += elem*listB[idx]
    return result


# In[2]:


listA = [1, 2, 3]
listB = [4, 5, 6]


# In[7]:


dotProduct(listA, listB)

