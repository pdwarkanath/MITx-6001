
# coding: utf-8

# In[18]:


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    for idx, elem in enumerate(L):
        L[idx] = elem[-1::-1]
    L[:] = L[-1::-1]
    return L


# In[20]:


L = [[1, 2], [3, 4], [5, 6, 7]]


# In[21]:


deep_reverse(L)

