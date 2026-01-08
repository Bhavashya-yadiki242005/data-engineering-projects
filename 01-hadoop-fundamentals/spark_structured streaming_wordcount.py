from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

# 1. Create Spark Session
spark = SparkSession.builder \
    .appName("SocketWordCount") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 2. Read streaming data from socket
lines = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# 3. Split lines into words
words = lines.select(
    explode(split(lines.value, " ")).alias("word")
)

# 4. Count words
counts = words.groupBy("word").count()

# 5. Define checkpoint location
checkpointDir = "/tmp/spark_checkpoint"

# 6. Write output to console
streamingQuery = counts.writeStream \
    .format("console") \
    .outputMode("complete") \
    .trigger(processingTime="5 seconds") \
    .option("checkpointLocation", checkpointDir) \
    .start()

# 7. Await termination
streamingQuery.awaitTermination()
