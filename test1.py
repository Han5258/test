#!/usr/bin/env python
# coding: utf-8

# In[59]:


soup=BeautifulSoup(open('yq.html',encoding='utf-8'),features='html.parser')


# In[60]:


import pandas as pd


# In[61]:


tables = soup.find_all('table')
 
print(len(tables))


# In[62]:


data = soup.find_all(name = 'script',attrs = {'id':'getListByCountryTypeService2true'})


# In[63]:


account = str(data)


# In[64]:


area = []
add = []
now = []
cure = []
die = []


# In[65]:


print(len(account))


# In[66]:


i=0
for a in account:
    if 'area' in data:
        area.append(data['area'])
    else:
        area.append('没有')
    if 'add' in data:
        add.append(data['add'])
    else:
        add.append('没有')
    if 'now' in data:
        now.append(data['now'])
    else:
        now.append('没有')
    if 'cure' in data:
        cure.append(data['cure'])
    else:
        cure.append('没有')
    if 'die' in data:
        die.append(data['die'])
    else:
        die.append('没有')


# In[67]:


data1 = pd.DataFrame(data)
data1.to_csv('a.csv')


# In[ ]:





# In[ ]:




