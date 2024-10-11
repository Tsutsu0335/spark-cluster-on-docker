from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession


print("heeeeeeeeeeeeeeeeeeeeeeeeloooooooooooooooooooooooo1")


conf = SparkConf().setAppName("Spark Test").setMaster("spark://127.0.0.1:7077")
spark = SparkSession.builder.config(conf=conf).getOrCreate()

print("heeeeeeeeeeeeeeeeeeeeeeeeloooooooooooooooooooooooo2")

# Loads data.
dataset = spark.createDataFrame([
(0.0, 0.0, 0.0),
(0.1, 0.1, 0.1),
(0.2, 0.2, 0.2),
(9.0, 9.0, 9.0),
(9.1, 9.1, 9.1),
(9.2, 9.2, 9.2),
], ["label1", "label2", "label3"])

dataset.show()