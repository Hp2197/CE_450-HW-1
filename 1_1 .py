
# coding: utf-8

# In[1]:


def if_function(a,b,c):
    if(a==True):
        return b
    else:
        return c
    
print(if_function(True,2,3))
print(if_function(False,2,3))
print(if_function(3==2,3+2,3-2))
print(if_function(3>2,3+2,3-2))

