#!/usr/bin/env python
# coding: utf-8

# In[58]:


#Assignment2: Functions


#The function has to accept one argument, if it is number, 
#it has to return whether it is odd or even number, if it is non number, 
#it has to return the data type of the argument passed

def func1(num1):
    if type(num1)== int or type(num1)==float:
        num1=int(num1)
        if (num1 % 2) == 0:
            print("{0} is an Even Number".format(num1))
        else:
            print("{0} is an Odd Number".format(num1))
    else:
        return type(num1)
    
    


# In[64]:


func('sss')


# In[65]:


func1(44.6)


# In[66]:


func1(123)


# In[67]:


func1(-3.5)


# In[68]:


func1(66)


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





# In[46]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[35]:





# In[39]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[34]:


func1(12)


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





# In[21]:


func1(12)


# In[ ]:





# In[ ]:





# In[17]:


def func(num1):
    if isinstance(num1, int):
        print("This is an integer")
    elif isinstance(num1, str):
        print("This is string")   
    else:
        print("This is not an integer nor string")


# In[18]:


func(12.5)


# In[ ]:





# In[16]:


func(12)


# In[ ]:





# In[ ]:





# In[13]:


func(12.5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[10]:


func(12.5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


func(12.7)


# In[6]:


func('abc')


# In[ ]:




