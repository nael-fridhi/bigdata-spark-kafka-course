# Mini-projet 

You work as a DataOps Engineer in a big financial company. In order to improve their products and services, you are tasked with building a development Big data Solution that will be used by machine learning engineers for trend analysis this environment will be used as a proof of concept to collect data from Twitter API and process the data then save them in a DFS for machine learning use cases.

- Technologies:
  - Data Storage: HDFS or S3 or Azure Blobl
  - Data Ingestion: Kafka
  - Data Processing: Spark
  - Data Pipelines: Airflow 

First, you need to deploy the infrastructure that we need to build this solution and configure the interaction between the different components.

**N.B:** You have the choice to use your local machine, docker containers or either Azure VMs or the service managed by Azure. 

Once you deployed the infrastructure you start developing the scripts for ingestion and processing and orchestration:

1. Develop a python program that scraps tweets from twitter using API and produces them into kafka topic
2. Develop a spark program which comsumes from the kafka topic process the data and save them into HDFS using 
3. Develop the airflow DAG that will run each 10 minutes.