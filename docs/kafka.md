# Apache Kafka Lab

## Installation Kafka

- We can install Kafka from binary 

```
wget http://apache.crihan.fr/dist/kafka/0.10.2.1/kafka_2.10-0.10.2.1.tgz
tar xzf kafka_2.10-0.10.2.1.tgz
cd kafka_2.10-0.10.2.1/

# Run zookeeper
./bin/zookeeper-server-start.sh ./config/zookeeper.properties

# Run Kafka Server 
./bin/kafka-server-start.sh ./config/server.properties
```
- We can also install Kafka using the confluent community package

```
wget -qO - https://packages.confluent.io/deb/5.2/archive.key | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/5.2 stable main"

sudo apt-get update && sudo apt-get install -y openjdk-8-jre-headless confluent-community-2.12

sudo systemctl start confluent-zookeeper

sudo systemctl enable confluent-zookeeper

sudo systemctl start confluent-kafka

sudo systemctl enable confluent-kafka

sudo systemctl status confluent*

kafka-topics --list --bootstrap-server localhost:9092

```

- We can also run kafka in docker 

```
curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-kafka/master/docker-compose.yml > docker-compose.yml
docker-compose up -d

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
## Run the velib Python Application

[Click Here!](../src/kafka/stations/README.m)



## Run the golang Producer sample 

1. Downlaod and install golang.
2. Verfiy the installation by running `go version`
3. Install the dependency kafka-go
4. Look at the file and verify if there is configuration to modify
5. Run the producer and check that the message produced to the topic by running a console consumer.
`go run Producer.go`

## Run the golang Consumer sample

1. Check the configuration to change in the consumer file 
2. Run the consumer and try to put records using a console producer and check if the consumer can consume your message
`go run Consumer.go`


[Golang Kafka Issue](https://github.com/confluentinc/confluent-kafka-go/issues/583)



