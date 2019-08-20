from pyspark import SparkContext

sc = SparkContext(master='local',appName='Spark Demo')

print(sc.textFile('/home/aashuotsh/Work/Tools.txt').first())
