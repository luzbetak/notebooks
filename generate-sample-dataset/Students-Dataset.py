# Databricks notebook source
# MAGIC %pip install faker

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from faker import Faker

fake = Faker()

student_schema = StructType([
    StructField("student_id",   IntegerType(), True),
    StructField("first_name",   StringType(), True),
    StructField("last_name",    StringType(), True),
    StructField("email",        StringType(), True),
    StructField("phone_number", StringType(), True),
    StructField("address",      StringType(), True),
])

sample_data = [(i, fake.first_name(), fake.last_name(), fake.email(), fake.phone_number(), fake.address()) for i in range(0, 10000)]
student_df = spark.createDataFrame(sample_data, schema=student_schema)
student_df.show(5, truncate=False)


# COMMAND ----------

# Write Data
table_catalog = "development"
table_schema  = "node_process_integrated"
table_name    = "students"
students      = f"{table_catalog}.{table_schema}.{table_name}"

student_df.write.mode("overwrite").saveAsTable(students)
spark.sql(f"SELECT * FROM {students} LIMIT 10").show(truncate=False)

# COMMAND ----------

# Write Data
table_catalog = "development"
table_schema  = "node_process_integrated"
table_name    = "students"
students      = f"{table_catalog}.{table_schema}.{table_name}"

spark.sql(f"SELECT * FROM {students} ORDER BY RAND() LIMIT 10").show(truncate=False)


# COMMAND ----------

table_df = spark.table(students)
table_df.printSchema()
