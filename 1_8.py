
# coding: utf-8

# In[4]:


def double_5(n):
    
    while(n//10 != 0):
        
        a=n%10
        
        n=n//10
        
        if(a==5):
            
            return n%10 == 5
        
        return False


# In[6]:


double_5(55)

