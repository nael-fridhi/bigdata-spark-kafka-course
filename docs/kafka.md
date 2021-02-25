# Apache Kafka Lab

## Installation Kafka
```
wget http://apache.crihan.fr/dist/kafka/0.10.2.1/kafka_2.10-0.10.2.1.tgz
tar xzf kafka_2.10-0.10.2.1.tgz
cd kafka_2.10-0.10.2.1/

# Run zookeeper
./bin/zookeeper-server-start.sh ./config/zookeeper.properties


# Run Kafka Server 
./bin/kafka-server-start.sh ./config/server.properties


```
## Create topic using command line

```
# Create a topic
./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic blabla

# Describe a topic 
./bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic blabla

# Produce a message to a topic using the command line 
./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic blabla

# Consume message from a topic using cmd
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic blabla

# Consume message using consumer group
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic blabla --consumer-property group.id=mygroup

# List consumer groups 
./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

# Describe consumer groups 
./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group mygroup

# Change a topic partition
./bin/kafka-topics.sh --alter --zookeeper localhost:2181 --topic blabla --partitions 2
```


## Run the golang Producer sample 



## Run the golang Consumer sample



## Run the golang kafka Stream sample


