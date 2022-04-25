#!/usr/bin/env python
# coding: utf-8

# In[36]:


f=open(r"C:\long.txt","r")


# In[37]:


a=f.readlines()


# In[38]:


for each in a:
    each=each.strip('\n')
    print(each+" ")


# In[ ]:





# In[39]:


a = [] 
with open(r'C:\long.txt' ,'r') as f:
    for line in f:
     a.append(line.strip().split(',')[0]) 
    print(a) 


# In[35]:





# In[24]:





# In[ ]:




