#!/usr/bin/env python
# coding: utf-8

# In[1]:


#problem 5
import numpy as np
fuhao=["","+","-"]
def Find_expression(x):
    cisu=0
    for a in fuhao:
        for b in fuhao:
            for c in fuhao:
                for d in fuhao:
                    for e in fuhao:
                        for f in fuhao:
                            for g in fuhao:
                                for h in fuhao:
                                    s="1"+a+"2"+b+"3"+c+"4"+d+"5"+e+"6"+f+"7"+g+"8"+h+"9"
                                    if eval(s)==x:
                                        cisu=cisu+1
                                        print(s)
    return cisu
x=int(input("x"))
Find_expression(x)


#problem 5.2
import numpy as np
fuhao=["","+","-"]
def Find_expression(x):
    cisu=0
    for a in fuhao:
        for b in fuhao:
            for c in fuhao:
                for d in fuhao:
                    for e in fuhao:
                        for f in fuhao:
                            for g in fuhao:
                                for h in fuhao:
                                    s="1"+a+"2"+b+"3"+c+"4"+d+"5"+e+"6"+f+"7"+g+"8"+h+"9"
                                    if eval(s)==x:
                                        cisu=cisu+1
    return print(cisu)
for i in range(1,101):
    Find_expression(i)


# In[ ]:




