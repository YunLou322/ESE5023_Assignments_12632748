#!/usr/bin/env python
# coding: utf-8

# In[1]:


#problem 1
def Print_values(a,b,c):
    if a>b  :
        if b>c:
            print(a,b,c)
        else:
            if a>c  : 
                print(a, c,b)
            else:
                print(c,a,b)
    else  :
        if b>c:
            print("nan")
        else:
            print(c,b,a)
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
Print_values(a,b,c)


# In[ ]:





# In[ ]:




