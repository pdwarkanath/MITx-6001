
# coding: utf-8

# In[16]:


def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    n = len(L)
    def fn(x):
        result = 0
        for r, a in enumerate(L):
            result += a*x**(n-r-1)
        return result
    return fn


# In[17]:


L = [1, 2, 3, 4]
x = 10


# In[18]:


general_poly(L)(x)

