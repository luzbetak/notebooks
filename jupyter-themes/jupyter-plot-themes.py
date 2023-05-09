#!/usr/bin/env python
# coding: utf-8

# In[10]:


#---------------------------------------------------------#
# https://github.com/dunovank/jupyter-themes
# https://seaborn.pydata.org/tutorial/aesthetics.html
#---------------------------------------------------------#
# !python3 -m pip install jupyterthemes
# !python3 -m pip install seaborn
#---------------------------------------------------------#


# In[2]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


from jupyterthemes import jtplot
jtplot.style(theme='onedork')


# In[4]:


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
        
sinplot()        


# In[5]:


sns.set()
sinplot()


# In[6]:


sns.set_style("whitegrid")
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.boxplot(data=data);


# In[7]:


sns.set_style("dark")
sinplot()


# In[8]:


f, ax = plt.subplots()
sns.violinplot(data=data)
sns.despine(offset=10, trim=True);


# In[9]:


f = plt.figure(figsize=(6, 6))
gs = f.add_gridspec(2, 2)

with sns.axes_style("darkgrid"):
    ax = f.add_subplot(gs[0, 0])
    sinplot()

with sns.axes_style("white"):
    ax = f.add_subplot(gs[0, 1])
    sinplot()

with sns.axes_style("ticks"):
    ax = f.add_subplot(gs[1, 0])
    sinplot()

with sns.axes_style("whitegrid"):
    ax = f.add_subplot(gs[1, 1])
    sinplot()

f.tight_layout()


# In[ ]:




