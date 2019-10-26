
# coding: utf-8

# In[5]:


import math
def foo(a,b,c,d):
    e=[a,b,c,d]
    min1=a
    min2=b
    i=0
    while(i<4):
        if e[i]<min1:
            min1=e[i]
        i=i+1
    i=0
    while(i<4):
        if(e[i]>min1 and e[i]<min2):
            min2=e[i]
            i=i+1
        print(min1,min2)
        return pow(min1,2)+pow(min2,2)
print(foo(1,2,3,4))
            

