<h1>PySpark, Delta Lake, Apache Arrow, Pandas</h1>

<table>
<tr>
<td><img src="https://spark.apache.org/docs/latest/api/python/_static/spark-logo-reverse.png" width="200" height="100" /></td>
<td><img src="https://delta.io/static/delta-lake-logo-a1c0d80d23c17de5f5d7224cb40f15dc.svg" width="200" height="100" /></td>
<td><img src="https://arrow.apache.org/img/arrow-inverse-300px.png" width="200" height="100" /></td>
</tr>
<table>

1. Simple getting started with PySpark and Delta Lake
2. [Quickstart: DataFrame](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html)
3. [Quickstart: Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html)
4. [PySpark SQL and Dataframes](https://spark.apache.org/docs/latest/sql-programming-guide.html)
5. [RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
6. [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
7. [Spark Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
8. [Machine Learning Library (MLlib) Guide](https://spark.apache.org/docs/latest/ml-guide.html)
9. [Delta Tables](https://docs.delta.io/latest/delta-intro.html)






* run pyspark --packages io.delta:delta-core_2.11:0.4.0 in commandline and see if the spark is browsable
* At the time of writing this notebook used spark which is only compatible with Java JDK 17. so had to uninstall openjdk@23 and also set the JAVA_HOME using:
  * nano ~/.bashrc
  * nano ~/.zshrc
  * nano ~/.bash_profile