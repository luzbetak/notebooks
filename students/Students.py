#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pyspark
# sc.setLogLevel("ERROR")


# In[5]:


df = spark.read.csv('students.csv', header='true')
print(type(df))


# In[ ]:


df.printSchema()


# In[ ]:


df.createOrReplaceTempView("students")


# In[ ]:


SQL = """
SELECT ethnicity, count(ethnicity) as total 
FROM students 
GROUP BY ethnicity 
ORDER BY total DESC
"""

df1 = spark.sql(SQL)
df1.show(10, False)


# In[ ]:


SQL = """
SELECT first_name, last_name, entry_academic_period
FROM students 
"""

df2 = spark.sql(SQL)
df2.show(10, False)


# In[ ]:




