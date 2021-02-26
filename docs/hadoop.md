# Hadoop Lab


## Hadoop Installation

- To avoid the difference between envrionment and Operating systems we will work with docker. So first, we will install docker. Then we will download the hadoop docker image which contains a standalone hadoop cluster that allows us to run hdfs command and hadoop mapreduce applications.

1. Follow the docker documentation link to install docker depending on your Operating system
[https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
  - You can execute this commands to run docker without `sudo`:
    - `sudo usermod -aG docker $USER`
    - `newgrp docker`
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

4. Open two terminal session: 
  - One for the hadoop container
  - One for the Host Machine

5. In the Host Machine terminal 
    - Create a folder **ynov**: `mkdir ynov`
    - `cd ynov`
    - clone the git project into this folder:
      `git clone https://github.com/nael-fridhi/bigdata-spark-kafka-course.git`

6. In the container terminal
    - Go to the Hadoop installation folder: `cd /usr/local/hadoop`
    - create a folder **ynov**: ``mkdir ynov`

7. Copy the folder form the Host machine to the Docker container:
    `docker cp`
**N.B:** We can do this sync using docker volumes 


## HDFS 

- In the container terminal try some commands to get familirized with the hdfs cli

```
# Get the documentation of hdfs dfs command
hdfs dfs -help
# Returns the contents of the path in HDFS 
hdfs dfs -ls <path>
# Move a file from HDFS src to HDFS dst
hdfs dfs -mv <src> <dst>
# Displays the file content
hdfs dfs -cat <src>
# Copy file from the Local to HDFS 
hdfs dfs -copyFromLocal <localsrc> ... <dst>
# Copy multiple path from local to HDFS 
hdfs dfs -put <localsrc> ... <dst>
# Create a folder in HDFS FS
hdfs dfs -mkdir <path>
# Copy a file from HDFS to the local
hdfs dfs -copyToLocal <src> <localdst>
# Remove a file from HDFS file system
hdfs dfs -rm -f -r <path>
```

## MapReduce WordCount

### Java

```
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath)

# This command shoud executed where you put the .java file of the mapreduce appplication
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