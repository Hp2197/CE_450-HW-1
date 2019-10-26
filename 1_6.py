
# coding: utf-8

# In[1]:


def pfct_num(m):
    i=0
    total=0
    while(i<m):
        total+=i
        if(total==m):
            return True
        if(total>m):
            return False
        i+=1
print( pfct_num(8))
print( pfct_num(28))
        

