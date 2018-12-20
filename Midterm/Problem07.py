
# coding: utf-8

# In[38]:


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    inter_keys = set(d1.keys()).intersection(d2.keys())
    f_inter = {}
    for i in inter_keys:
        f_inter[i] = f(d1[i], d2[i])
    
    f_diff = {}
    for i in d1.keys():
        if i not in inter_keys:
            f_diff[i] = d1[i]
    for j in d2.keys():
        if j not in inter_keys:
            f_diff[j] = d2[j]
    
    return f_inter, f_diff


# In[39]:


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}


# In[40]:


def f(a, b):
    return a > b
dict_interdiff(d1, d2)

