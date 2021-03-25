# Apache Airflow

## Installation 

We can install Airflow using docker or manually:

### Docker using Astro:

[https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart)


### Docker native

```curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml' 
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
docker-compose up airflow-init

```
### Manually 

1. Make sure you've python 3.6+ installed on your computer.
2. the official way if installing airflow is with Pip.
3. On Linux, you have to install certain operating system dependencies as shown below

    ```sudo apt-get install -y --no-install-recommends \
            freetds-bin \
            krb5-user \
            ldap-utils \
            libffi6 \
            libsasl2-2 \
            libsasl2-modules \
            libssl1.1 \
            locales  \
            lsb-release \
            sasl2-bin \
            sqlite3 \
            unixodbc```

4. Installing Airflow : `pip install apache-airflow`

That's not the best way. Indeed, Airflow bring MANY dependencies.
The problem is, if one dependency is updated, the previous command will install the latest version which may cause dependency incompatibilities and errors.

```pip install apache-airflow --constraint https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt```

You can change the installation path by setting this environment variable: `AIRFLOW_HOME=/opt/airflow`

**DB init:** Once you're good with your Airflow home, initialize Airflow with:

`airflow db init`

- default user/password airflow: admin/admin or airflow/airflow



## Reminder 

- Apache Airflow is an open source platform to programmatically author, schedule and monitor workflows.
  - Dynamic
  - Scalable
  - Interactive
  - REST API
  - Extensible
  - Not a streaming or a data processing framework


### Core Components  

- Airflow Consist of several components:

  - Web Server: Flask UI HTTP Server provides access to DAG/task status information
  - Scheduler: The heart of Airflow Responsible for adding the necessary tasks to the queue
  - Metadata Databases: SQL Alchemy Contains information about the status of tasks, DAGs, Variables, connections, etc.
  - Executor: How your tasks are going to be exectued on Airflow (There is a queue behind each executor) 
  - Worker: Where your tasks are executed 


### DAGs

- **Operators:** A type of task to execute in your data pipeline/DAG:
  - Action Operators: Allow you to execute python function/ bash command for example 
  - Transfer Operators: Transfer data from a source to a destination
  - Sensor Operators: Wait for something

- **Task** Instance of an Operator

- **Task Instance** Represents a specific run of a task: DAG + TASK + Point in time


- **Dependencies:** The edges in a DAG those are the dependencies

- set_upstream OR set_downstream, << OR >>


Workflow: A DAG with operator and dependencies 

**Task Lifecycle:** scheduled, queued, running, success

1. A new python file dag.py 
2. File will be parsed by the web server (30 seconds per default) and scheduler (every 5 minutes per default)
3. Scheduler create a DagRun Object 



### Extras and providers

Extras and providers are tools to be installed to the airflow server in order to interact with other systems like postgres provider or kubernetes extras.

### Others

Interacting with Airflow:

- UI: Manage and monitor your data pipeline
- CLI: Test tasks or upgrade airflow or initialize airflow
- REST API: Build something on top of Airflow or trigger DAG programmatically 


- DAG:
  - Tree View: Get the history and DAG run
  - Graph View: Check the dependency of your data pipeline as well as the status of task for the latest DAG run and it shows you also which operator is used for each task.
  - Gantt View: Analyse task duration as well as overlaps (tasks running in parallel for example)


- CLI: Most important Commands:
  - airflow db init: initialize the database and generate the folders and files 
  - airflow db upgrade: upgrade airflow metadata
  - airflow db reset: remove everything in the database
  - airflow scheduler
  - airflow web-server
  - airflow celery worker
  - airflow dags unpause
  - airflow dags pause
  - airflow dags trigger 
  - airflow dags list
  - airflow tasks list <dag_id>
  - airflow tasks test: Used when we want to add task to make sure it works
  - airflow dags backfill -s <start-date> -e <end-date> --reset_dagruns: rerun past dag runs


- By default dag scheduled every 24 hours

- The dag will triggered after start date + the schedule interval. once the dag runs the execution date becomes the start date and the new start date becomes start date + the schedule interval. 

- It's not recommended to use dynamic start date

- The process of backfilling allows you to run or rerun past not triggered or already triggered dag runs

- The most commonly used operator in airflow:
  - DummyOperator
  - PythonOperator
  - BashOperator

- We can exchange data between tasks in Airflow using Xcoms 
- Xcoms is stored in the database of airflow 


- Airflow Executor: The way your tasks are going to be executed in your airflow instances
  - LocalExecutor: limitation is the resources that you have in your local machine
  - SequentialExecutor: debug tasks, experiemtal purposes, can execute only one task at the same time
  - KubernetesExecutor:
  - CeleryExecutor:


- PARALLELISM parameter ( default 32 ) : define the number of tasks that could be run in your entire airflow instances.
- DAG_CONCURRENCY ( default 16 ) : define the number of tasks for a given dag that can be executed in parallel across all of dag runs.
- MAX_ACTIVE_RUNS_PER_DAG (default 16) : The number of dag runs that can run at the same time for a given dag.
- MAX_ACTIVE_RUNS : 
- CONCURRENCY : Only a one task could be run in all dag runs of a specific dag.

- start_date vs execution_date
- catchup vs backfill

