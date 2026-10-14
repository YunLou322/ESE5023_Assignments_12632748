#!/usr/bin/env python
# coding: utf-8

# In[3]:


#problem 4
def Least_moves(x):
    if x>=64:
        a=64
        cisu=6
    elif x>=32:
        a=32
        cisu=5
    elif x>=16:
        a=16
        cisu=4
    elif x>=8:
        a=8
        cisu=3
    elif x>=4:
        a=4
        cisu=2
    elif x>=2:
        a=2
        cisu=1
    else:
        a=1
        cisu=0
    yushu=x-a
    if yushu>=32:
        yushu=yushu-32
        cisu=cisu+1
    if yushu>=16:
        yushu=yushu-16
        cisu=cisu+1
    if yushu>=8:
        yushu=yushu-8
        cisu=cisu+1
    if yushu>=4:
        yushu=yushu-4
        cisu=cisu+1
    if yushu>=2:
        yushu=yushu-2
        cisu=cisu+1
    if yushu>=1:
        yushu=yushu-1
        cisu=cisu+1
    print(cisu)
x=int(input("输入"))
Least_moves(x)


# In[ ]:




