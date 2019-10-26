
# coding: utf-8

# In[ ]:


def uniq_digits(x):
  a=[0,1,2,3,4,5,6,7,8,9]
  i=0
  while(x>0):
    a[i]=x%10
    i+=1
    x=x//10
  c=i
  i-=1
  while(i>0):
    b=0
    while(b<i):
      if(a[b]!=a[i]):
        b+=1
      else:
        b=0
        i-=1
        c-=1
    i-=1
  return c


# In[ ]:


uniq_digits(1313131)

