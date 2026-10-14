#!/usr/bin/env python
# coding: utf-8

# In[3]:


#problem 3
import numpy as np
def Pascal_triangle(k):
    A=np.ones(1)
    for i in range(1,k):
        B=np.ones(i+1)
        for j in range(1,i):
            B[j]=A[j-1]+A[j]
        A=B
    print(A)
x=100
y=200
Pascal_triangle(x)
Pascal_triangle(y)


# In[ ]:




