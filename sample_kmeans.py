from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("Spark Test").setMaster("spark://127.0.0.1:7077")
spark = SparkSession.builder.config(conf=conf).getOrCreate()

# Loads data.
dataset = spark.read.format("libsvm").load("/opt/spark/data/mllib/sample_kmeans_data.txt")

# Trains a k-means model.
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(dataset)

# Make predictions
predictions = model.transform(dataset)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)