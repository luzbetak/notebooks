#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !python3 -m pip install pyspark
# !pip install pandas
# !python3 -m pip install --upgrade pip
# !python -V


# In[2]:


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import functions as f


# In[3]:


data1 = [
    (1, "AA"), \
    (2, "AB"), \
    (3, "BB"), \
    (4, "BA"), \
    (5, "AA"), \
    (6, "AB")
  ]


# In[4]:


columns= ["col1","col2"]


# In[5]:


spark = SparkSession.builder.appName('GroupBy').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")


# In[6]:


df = spark.createDataFrame(data = data1, schema = columns)


# In[7]:


df1 = df.filter(df.col2 == "AA")                 \
      .groupBy("col2")                           \
      .count()                                   \
      .withColumnRenamed("count", "count_rows")


# In[8]:


df1.printSchema()
df1.show(truncate=False)


# In[11]:


df1.write.mode('overwrite').csv("filter-group-by.csv")

# df2.write.format("csv").mode('overwrite').save("filter-group-by.csv")


# In[ ]:




