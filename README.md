# **E2E-ML-Project-with-MLflow & DVC**

## Project Overview

This project demonstrates an end-to-end machine learning pipeline using **MLflow** for tracking experiments and **DVC** (Data Version Control) for managing datasets and model versions. The pipeline includes configuration management, logging, and deployment automation using AWS services like EC2 and ECR, integrated with GitHub Actions for CI/CD.

## Workflows

1. Update `config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline
8. Update `main.py`
9. Update `app.py`
10. Update DVC

![Alt Text](https://github.com/MalikZeeshan1122/Machine-learning-Project-MLflow/blob/main/WhatsApp%20Image%202024-09-29%20at%2011.58.52%20AM.jpeg)

## How to run?

### STEPS:

1. **Clone the repository**

```bash
git clone https://github.com/tiksharsh/mlflow-project.git
STEP 01: Create a conda environment after opening the repository
bash
Copy
Edit
conda create -n mlproj-venv python=3.10.9 -y
conda activate mlproj
STEP 02: Install the requirements
bash
Copy
Edit
pip install -r requirements.txt
Finally, run the following command:

bash
Copy
Edit
python app.py
Now, open up your local host and port to see the application in action.

MLflow
For more information, refer to the official MLflow Documentation

To run MLflow UI
bash
Copy
Edit
mlflow ui
dagshub
dagshub

Use the following code to initialize your project with dagshub and log your MLflow metrics:

python
Copy
Edit
import dagshub
dagshub.init(repo_owner='malikzeeshan3.1417', repo_name='mlflow-project', mlflow=True)

import mlflow
with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)
Run this to export environment variables:

bash
Copy
Edit
export MLFLOW_TRACKING_URI=https://dagshub.com/malikzeeshan3.1417/mlflow-project.mlflow
export MLFLOW_TRACKING_USERNAME=malikzeeshan3.1417
export MLFLOW_TRACKING_PASSWORD=0f27aa886d82f4cd2f16dc79464402ddf1de99b
AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS Console
2. Create IAM User for Deployment
EC2 Access: It is a virtual machine.

ECR: Elastic Container Registry to save your Docker image in AWS.

Deployment Description
Build Docker image of the source code.

Push your Docker image to ECR.

Launch your EC2 instance.

Pull your image from ECR in EC2.

Launch your Docker image in EC2.

Policies for IAM User
AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess

3. Create ECR Repository to Store Docker Image
Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

4. Create EC2 Machine (Ubuntu)
5. Open EC2 and Install Docker in EC2 Machine
bash
Copy
Edit
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
6. Configure EC2 as a Self-hosted Runner
Go to GitHub settings > Actions > Runners > New Self-hosted Runner > Choose OS > Follow the setup commands.

7. Set up GitHub Secrets
AWS_ACCESS_KEY_ID=your_access_key

AWS_SECRET_ACCESS_KEY=your_secret_key

AWS_REGION=us-east-1

AWS_ECR_LOGIN_URI=your_ecr_uri

ECR_REPOSITORY_NAME=simple-app

About MLflow
MLflow is production-grade and provides tools to track experiments and manage models.

It helps in logging, tagging, and tracking all machine learning experiments.

👨‍💻 Author
Malik Muhammad Zeeshan
Machine Learning Engineer | Data Scientist

📧 Email: malikzeeshan3.1417@gmail.com
🔗 LinkedIn: @muhammadzeeshan007
🐙 GitHub: MalikZeeshan1122

📄 License
This project is licensed under the MIT License.

🙏 Acknowledgments
Special thanks to the contributors and open-source libraries that make this project possible. Also, thanks to MLflow for providing a great framework for tracking and managing machine learning workflows.

vbnet
Copy
Edit


In this version, I've added the **project name** "E2E-ML-Project-with-MLflow & DVC" at the beginning and made sure your contact information is included.
