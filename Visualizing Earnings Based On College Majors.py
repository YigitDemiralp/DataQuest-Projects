#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

recent_grads = pd.read_csv('recent-grads.csv')

print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())

print(recent_grads.shape)
recent_grads = recent_grads.dropna()
print(recent_grads.shape)


# In[3]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# In[4]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')


# In[5]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# In[6]:


recent_grads.plot(x='ShareWomen', y='Employed', kind='scatter')


# In[7]:


recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[8]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# In[29]:


recent_grads['Sample_size'].hist(bins = 25, range = (0,2000))


# In[20]:


recent_grads['Median'].hist()


# In[21]:


recent_grads['Employed'].hist(bins=25, range=(0,5000))


# In[22]:


recent_grads['Full_time'].hist(bins=25, range=(0,5000))


# In[23]:


recent_grads['ShareWomen'].hist()


# In[24]:


recent_grads['Unemployment_rate'].hist()


# In[25]:


recent_grads['Men'].hist(bins=25, range=(0,5000))


# In[26]:


recent_grads['Women'].hist(bins=25, range=(0,5000))


# # Scatter Matrix

# In[31]:


from pandas.plotting import scatter_matrix 
scatter_matrix(recent_grads[['Sample_size', 'Median']])


# In[32]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']])


# # Bar Plots

# In[38]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen')
recent_grads.tail(10).plot.bar(x='Major', y='ShareWomen')


# In[39]:


recent_grads.head(10).plot.bar(x='Major', y='Unemployment_rate')
recent_grads.tail(10).plot.bar(x='Major', y='Unemployment_rate')


# In[ ]:


recent_grads.plt.hexbin(x='Sample_size', y='Median')

