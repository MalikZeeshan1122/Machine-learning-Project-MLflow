# Machine-learning-Project-with-MLflow
# E2E-ML-Project-with-MLflow-&-DVC

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py
10. Update the DVC
11. 
![Alt Text](https://github.com/MalikZeeshan1122/Machine-learning-Project-MLflow/blob/main/WhatsApp%20Image%202024-09-29%20at%2011.58.52%20AM.jpeg)
# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/tiksharsh/mlflow-project.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj-venv python=3.10.9 -y
```

```bash
conda activate mlproj
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up you local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd

- mlflow ui

### dagshub

[dagshub](https://dagshub.com/)
# Dags hub remote / experiments / tracking mlflow /copied /paste/ readme

import dagshub
dagshub.init(repo_owner='malikzeeshan3.1417', repo_name='mlflow-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

Run this to export as env variables:

```bash

# export MLFLOW_TRACKING_URI=https://dagshub.com/tiksharsh/mlflow-project.mlflow

# export MLFLOW_TRACKING_USERNAME=tiksharsh 

# export MLFLOW_TRACKING_PASSWORD=0f27aa886d82f4cd2f16dc79464402ddf1de99b

export MLFLOW_TRACKING_URI=https://dagshub.com/malikzeeshan3.1417/mlflow-project.mlflow

export MLFLOW_TRACKING_USERNAME=malikzeeshan3.1417

export MLFLOW_TRACKING_PASSWORD=0f27aa886d82f4cd2f16dc79464402ddf1de99b
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws

    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

## About MLflow

MLflow

- Its Production Grade
- Trace all of your expriements
- Logging & tagging your model
