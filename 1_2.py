
# coding: utf-8

# In[6]:


def sum_odd(a):
    if a==0:
        return 0   
    if(a%2==0):
        a=a-1
       
    if(a%2==1):
        return a+sum_odd(a-1)
    
b=sum_odd(6)
print(b)

