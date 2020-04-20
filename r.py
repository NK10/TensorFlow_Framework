# To find out where the pyspark
import findspark
findspark.init()
# Creating Spark Context
from pyspark import SparkContext
sc = SparkContext("local", "first app")
# Calculating words count
text_file = sc.textFile("readme.md")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
# Printing each word with its respective count
output = counts.collect()
for (word, count) in output:
    print("Nitin : %s: %i" % (word, count))
# Stopping Spark Context
sc.stop()