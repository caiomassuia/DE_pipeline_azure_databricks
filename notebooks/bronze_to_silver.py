# Databricks notebook source
dbutils.fs.ls('/mnt/dados/bronze')

# COMMAND ----------

path='dbfs:/mnt/dados/bronze/dataset_imoveis/'
df = spark.read.format('delta').load(path)

# COMMAND ----------

display(df)

# COMMAND ----------

display(df.select('anuncio.*'))

# COMMAND ----------

display(
    df.select('anuncio.*','anuncio.endereco.*')
)

# COMMAND ----------

df_detalhado = df.select('anuncio.*','anuncio.endereco.*')

# COMMAND ----------

display(df_detalhado)

# COMMAND ----------

df_silver = df_detalhado.drop('caracteristicas')

# COMMAND ----------

path_silver = 'dbfs:/mnt/dados/silver/dataset_imoveis'

df_silver.write.mode('overwrite')\
                .format('delta')\
                .save(path_silver)


# COMMAND ----------


