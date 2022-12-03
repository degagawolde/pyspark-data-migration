# pyspark-data-migration
Migrating data from different sources and putting them together.

## Spark

## PySpark
- install with 
```
pip install pyspark
```

- create spark session
```
import pyspark as spark
from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName("Python Spark SQL basic example")\
    .config("spark.some.config.option", "some-value")\
    .getOrCreate()
```

### Reading CSV
```
df1 = spark.read.options(header='True', inferSchema='True').csv("../data/annotation-1/annotation_database.csv")
print(df1.printSchema())
print((df1.count(), len(df1.columns)))
df2 = spark.read.options(header='True', inferSchema='True').csv("../data/annotation-2/annotation_database.csv")
print(df2.printSchema())
print((df2.count(), len(df2.columns)))
```

### Merging DataFrames
```
df = df1.union(df2)
print((df.count(), len(df.columns)))
```

### Removing Duplicates
```
df = df.dropDuplicates()
print((df.count(), len(df.columns)))
```
### Writing DataFrame to file.
```
df.write.option("header",True).csv("../data/annotation/annotation_database")
```

## Read More

- [Apache Spark](https://spark.apache.org/docs/latest/api/python/)
- [PySpark](https://spark.apache.org/docs/latest/api/python/development/contributing.html)
- [databricks](https://docs.databricks.com/external-data/csv.html)