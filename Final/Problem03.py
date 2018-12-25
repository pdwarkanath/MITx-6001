
# coding: utf-8

# In[3]:


trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}


# In[29]:


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    x  = int(us_num)
    if str(x) in trans:
        return trans[str(x)]
    elif us_num[1] == '0':
        return trans[us_num[0]] + ' shi'
    elif us_num[0] == '1':
        return 'shi ' + trans[us_num[1]]
    else:
        return trans[us_num[0]] + ' shi ' + trans[us_num[1]]    


# In[32]:


convert_to_mandarin('36')

