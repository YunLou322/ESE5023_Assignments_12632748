#!/usr/bin/env python
# coding: utf-8

# In[1]:


#problem 2
import numpy as np
M1 =np.random.randint(0,50 ,(5,10))
M2 =np.random.randint(0,50,(10,5))
M3=np.zeros((5,5))
def Matrix_multip(M1,M2):
    for i in range(5):
        for j in range(5):
            for k in range(10):
                M3[i,j]=M1[i,k]*M2[k,j]
    return M3
Matrix_multip(M1,M2)
print(M1)
print(M2)
print(M3)


# In[ ]:




