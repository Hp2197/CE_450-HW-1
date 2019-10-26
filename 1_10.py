
# coding: utf-8

# In[3]:


def sum(n):
    total=0
    i=1
    while(i<n):
        if n%i==0:
            total+=i
        i+=1
    return total
def amc(m):
    i=m+1
    while(1):
        a=sum(i)
        if i==sum(a):
            if i!=a:
                return i
        i+=1  


# In[4]:


amc(5)

