#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !python3 -m pip install pyspark
# !python3 -m pip install --upgrade pip
# !python3 -m pip install pandas
# !python -V


# In[2]:


import pandas as pd

data = {'product': ['computer', 'tablet', 'printer', 'laptop'],
        'price': [850, 200, 150, 1300] }

df = pd.DataFrame(data)

df.to_csv('export-dataframe-2.csv', index=False, header=True)

print(df)


# In[ ]:




