#!/usr/bin/env python
# coding: utf-8

# In[2]:


# using lambda print list of even and odd numbers from this list
# Using FILTER to filter the list. Filter takes two arguments (func, iterable)

list1=[1,2,4,5,6,76,8,9,10]

evens=list(filter(lambda n:n%2==0,list1))
print("The even numbers from the list are:",evens)

odds=list(filter(lambda n:n%2!=0,list1))
print("The odd numbers from the list are:",odds)


# In[8]:


# Using Map to change the value(Add, multiply or double) the list. Map takes two arguments (func, value/arg)

doubles=list(map(lambda n:n*2,list1))
print(doubles)


# In[12]:


# Using Reduce to may be get one value from the list. To use reduce, we need to sometimes use import reduce and functools to use it
# this REDUCE also takes two args, (func, sequence)
from functools import reduce
sum=reduce(lambda a,b:a+b,list1)
print(sum)


# In[17]:


#Summarize argument a, b, and c and return the result:

x= lambda a,b,c:a+b+c
print(x(5,3,4))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




