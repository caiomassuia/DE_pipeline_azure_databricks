# Databricks notebook source
# MAGIC %md
# MAGIC ## Verificando se os dados estao na pasta inbound

# COMMAND ----------

dbutils.fs.ls('/mnt/dados/inbound')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lendo os dados

# COMMAND ----------

path = 'dbfs:/mnt/dados/inbound/dados_brutos_imoveis.json'
df = spark.read.json(path)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Removendo colunas

# COMMAND ----------



# COMMAND ----------

df_anuncio = df.drop('imagens','usuario')

# COMMAND ----------

display(df_anuncio)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Criando uma coluna

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

df_bronze = df_anuncio.withColumn('id',col("anuncio.id"))
display(df_bronze)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Salvando na camada bronze

# COMMAND ----------

path_bronze = 'dbfs:/mnt/dados/bronze/dataset_imoveis'
df_bronze.write.mode('overwrite')\
                .format('delta')\
                .save(path_bronze)
