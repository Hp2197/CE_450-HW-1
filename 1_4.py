
# coding: utf-8

# In[7]:


import math
def df(a,b,c):
    d=[a,b,c]
    
    i,j,k=0,0,0
    
    while(i<3):
        j=0
        while(j<3):
            k=0
            while(k<3):
                print(i,j,k,(d[j])-(d[k]))
                if(d[i]==(d[j])-(d[k])):
                    return True
                k=k+1
            j=j+1
                
        i=i+1
                
    return False
print(df(5,3,2))            

