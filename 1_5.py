
# coding: utf-8

# In[1]:


i=0
def lrgst_factor(m):
    global i
    if((m+i)%(m-1)==0):
        i=0
        return (m-1)
    else:
        i+=1
    return lrgst_factor(m-1)


# In[2]:


lrgst_factor(15)

