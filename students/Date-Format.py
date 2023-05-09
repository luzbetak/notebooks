#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark
sc.setLogLevel("ERROR")


# Convert Date from 1901-12-25 to 12/25/1901 

# In[2]:


spark.sql("""
SELECT 
    DATE_FORMAT(
        CAST(TO_DATE(CAST("1901-12-25" AS DATE), 'yyyy-MM-dd') AS DATE), 'MM/dd/yyyy'
    ) AS DOB
""").show(10, vertical=True, truncate=False)


# In[ ]:




