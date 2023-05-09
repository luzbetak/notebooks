# Databricks notebook source
# MAGIC %pip install faker

# COMMAND ----------

# Cell 1: Import libraries
from faker import Faker
import random
from datetime import datetime
from pyspark.sql import Row 
from pyspark.sql.types import StringType, FloatType, IntegerType, DateType, StructType, StructField


# COMMAND ----------

# Cell 2: Generate fake products and sales data
fake = Faker()

def custom_sku():
    return f"{fake.random_number(digits=4)}-{fake.random_number(digits=4)}-{fake.random_number(digits=4)}"

def generate_products(n):
    products = []
    for _ in range(n):
        product = { 
            'product_id': custom_sku(),
            'name': fake.bs(),
            'description': fake.sentence(),
            'price': round(random.uniform(1, 500), 2), 
            'currency': fake.currency_code(),
            'barcode': fake.ean()
        }   
        products.append(product)
    return products


def generate_sales(products, n): 
    sales = []
    for _ in range(n):
        product = random.choice(products)
        sale_date = fake.date_between(start_date='-1y', end_date='today')
        sale = { 
            'product_id': product['product_id'],
            'quantity': random.randint(1, 10),
            'total_price': product['price'] * random.randint(1, 10),
            'sale_date': sale_date
        }   
        sales.append(sale)
    return sales

products = generate_products(100)
sales    = generate_sales(products, 100000)

# COMMAND ----------

# Cell 3: Convert Python data to PySpark DataFrames


products_schema = StructType([
    StructField('product_id',   StringType(), True),
    StructField('name',         StringType(), True),
    StructField('description',  StringType(), True),
    StructField('price',        FloatType(), True),
    StructField('currency',     StringType(), True),
    StructField('barcode',      StringType(), True)
])

sales_schema = StructType([
    StructField('product_id',   StringType(), True),
    StructField('quantity',     IntegerType(), True),
    StructField('total_price',  FloatType(), True),
    StructField('sale_date',    DateType(), True)
])

products_df = spark.createDataFrame(products, schema=products_schema)
sales_df = spark.createDataFrame(sales, schema=sales_schema)



# COMMAND ----------

# Cell 4: Save DataFrames as tables
table_catalog = "development"
table_schema  = "node_process_integrated"
products      = f"{table_catalog}.{table_schema}.products"
sales         = f"{table_catalog}.{table_schema}.sales"

spark.sql(f"DROP TABLE IF EXISTS  {products}")
spark.sql(f"DROP TABLE IF EXISTS  {sales}")

products_df.write.mode("overwrite").saveAsTable(products)
sales_df.write.mode("overwrite").saveAsTable(sales)

# COMMAND ----------

# Cell 6: Display data from sales table
table_catalog = "development"
table_schema  = "node_process_integrated"
products      = f"{table_catalog}.{table_schema}.products"
sales         = f"{table_catalog}.{table_schema}.sales"

spark.sql(f"SELECT * FROM {products} ORDER BY RAND() LIMIT 5").show(truncate=False)
spark.sql(f"SELECT * FROM {sales}    ORDER BY RAND() LIMIT 5").show(truncate=False)
