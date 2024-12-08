![Jupyter workflow](https://github.com/blitznihar/SparkWithoutDatabricks/actions/workflows/build-and-test.yml/badge.svg)


<table>
<tr>
<td><img src="https://spark.apache.org/docs/latest/api/python/_static/spark-logo-reverse.png" width="100" height="50" /></td>
<td><img src="https://user-images.githubusercontent.com/25181517/183914128-3fc88b4a-4ac1-40e6-9443-9a30182379b7.png" width="100" height="100" /></td>
<td><img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" width="100" height="100" /></td>
<td><img src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png" width="100" height="100" /></td>
<td><img src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" width="100" height="100" /></td>
 <td><img src="https://arrow.apache.org/img/arrow-inverse-300px.png" width="100" height="100" /></td>
</tr>
<table>

<h1>PySpark, Delta Lake, Apache Arrow, Pandas</h1>

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
