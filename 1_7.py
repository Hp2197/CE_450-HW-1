
# coding: utf-8

# In[1]:


def same_ord(a,b):
    i,j = 0,0
    while(a//10 != 0):
        a = a//10
        i+=1
    while(b//10 != 0):
        b = b//10
        j+=1
        
    return i==j


# In[2]:


same_ord(50,70)

