
# coding: utf-8

# In[70]:


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here
    
    inc_len = 0
    dec_len = 0
    max_len = 0

    
    for i in range(len(L)-1):
        if L[i+1] >= L[i]:
            inc_len += 1
            if inc_len > max_len:
                max_len = inc_len
                end_pos = i+1
        else:
            inc_len = 0

        if L[i+1] <= L[i]:
            dec_len += 1
            if dec_len > max_len:
                max_len = dec_len
                end_pos = i+1     
        else:
            dec_len = 0
        
    return sum(L[end_pos-max_len:end_pos+1])
    


# In[72]:


L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]


# In[73]:


longest_run(L)

