# Hadoop Lab


## Hadoop Installation

- To avoid the difference between envrionment and Operating systems we will work with docker. So first, we will install docker and after that we will download we docker image contains image to run work with and run some hdfs and hadoop mapreduce command.

1. Follow the docker documentation link to install docker depending on your Operating system
[https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
2. Once docker installed, run this command to download the hadoop image:
  - `docker pull sequenceiq/hadoop-docker:2.7.0` : this command download the docker image in local
  - `docker run -it sequenceiq/hadoop-docker:2.7.0 /etc/bootstrap.sh -bash`: This command run a docker container from the image download in the previous command
3. You can test whether the container works well or not by running this commands: 

    ```
    cd $HADOOP_PREFIX
    # run the mapreduce
    bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar grep input output 'dfs[a-z.]+'
    # check the output
    bin/hdfs dfs -cat output/*
    ```


## HDFS 


```
hdfs dfs -help
hdfs dfs -ls <path>
hdfs dfs -mv <src><dst>
hdfs dfs -cat <src>
hdfs dfs -copyFromLocal <localsrc> ... <dst>
hdfs dfs -put <localsrc> ... <dst>
hdfs dfs -mkdir <path>
hdfs dfs -copyToLocal <src> <localdst>
hdfs dfs -rm -f -r <path>
```

## MapReduce WordCount

### Java

```
export HADOOP_CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath)
javac -classpath $HADOOP_CLASSPATH WordCount*.java
mkdir wordcount
mv *.class wordcount/
jar -cvf wordcount.jar -C . wordcount
hadoop jar wordcount.jar wordcount.WordCountDriver /input/test.txt /results
```

### Python
```
hadoop jar hadoop-streaming.jar -input /lejourseleve.txt -output /results -mapper ./WordCountMapper.py -reducer ./WordCountReducer.py
```