# Apache Storm Lab 


## Installation


1. Install Java: </br>
`sudo apt install default-jre`

2. Install Maven:
    ```
    cd /opt
    wget https://downloads.apache.org/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
    tar -zxvf apache-maven-3.6.3-bin.tar.gz
    export PATH=/opt/apache-3.6.3/bin:$PATH
    source .bashrc
    # Test the maven installation
    mvn version
    ```

3. Storm installation 
  - **Docker:**
    - `docker-compose -f storm.yaml up -d`
  - **Local Machine:**
    - Install Zookeeper
        ```
        $ cd /opt
        $ wget https://downloads.apache.org/zookeeper/zookeeper-3.6.2/apache-zookeeper-3.6.2-bin.tar.gz
        $ tar -xvf apache-zookeeper-3.6.2-bin.tar.gz
        $ cd zookeeper-3.6.2
        $ mkdir data
        $ vi conf/zoo.cfg
        tickTime=2000
        dataDir=/path/to/zookeeper/data
        clientPort=2181
        initLimit=5
        syncLimit=2
        # Run Zookeepr 
        $ bin/zkServer.sh start
        ``` 

    - Install Storm
        ```
        $ cd /opt
        $ tar -zxf apache-storm-0.9.5.tar.gz
        $ cd apache-storm-0.9.5
        $ mkdir data
        
        # Start Nimbus
        $ bin/storm nimbus
        
        # Start Supervisor 
        $ bin/storm supervisor

        # Start UI
        $ bin/storm ui
        ```

## Run a Java topology application in a storm cluster


```
storm jar <path-to-your-jar-file.jar>  <the-java-class-of-the-topology>

Example: 
storm storm jar /analytics-1.0-SNAPSHOT.jar analytics.App

```