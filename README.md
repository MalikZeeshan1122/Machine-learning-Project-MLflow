# E2E-ML-Project with MLflow & DVC 🚀

![MLflow](https://img.shields.io/badge/MLflow-%23FF6F00.svg?style=for-the-badge&logo=mlflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-%2395C93D.svg?style=for-the-badge&logo=dvc&logoColor=white)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Project Overview

**E2E-ML-Project-with-MLflow & DVC** is a comprehensive end-to-end machine learning pipeline demonstrating the full ML lifecycle:

- **Model training** 🏋️
- **Experiment tracking** 🔍
- **Version control** 🔄
- **Deployment** 🚀

### ✨ Key Features
- **MLflow** for experiment tracking
- **DVC** for data versioning
- **GitHub Actions** CI/CD
- **AWS** deployment (EC2/ECR)
- **Dockerized** environment
- **Dagshub** integration

---

## 📖 Table of Contents
1. [Project Setup](#-project-setup)
2. [How to Run](#-how-to-run)
3. [MLflow Integration](#-mlflow-integration)
4. [DVC Integration](#-dvc-integration) 
5. [Deployment](#-deployment-instructions)
6. [Tech Stack](#-technologies-used)
7. [Contact](#-contact-information)
8. [Acknowledgments](#-acknowledgments)

---

## 🛠️ Project Setup

### Prerequisites
- Python 3.10+
- Conda/Miniconda
- Git
- Docker

### Installation
```bash
# 1. Clone repository
git clone https://github.com/tiksharsh/mlflow-project.git
cd mlflow-project

# 2. Create conda environment
conda create -n mlproj python=3.10.9 -y
conda activate mlproj

# 3. Install dependencies
pip install -r requirements.txt
▶️ How to Run
bash
Copy
# Start MLflow tracking server
mlflow server --backend-store-uri sqlite:///mlflow.db \
             --default-artifact-root ./artifacts \
             --host 0.0.0.0

# Run main pipeline (in another terminal)
python app.py
Access UI at: http://localhost:5000

🔍 MLflow Integration
Basic Tracking
python
Copy
import mlflow

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
UI Access
bash
Copy
mlflow ui --port 5000
🔄 DVC Integration
Workflow
bash
Copy
# Initialize
dvc init

# Add data
dvc add data/raw_dataset.csv

# Configure remote (AWS S3 example)
dvc remote add -d myremote s3://mybucket/dvc-storage

# Version data
dvc push
☁️ Deployment Instructions
AWS CI/CD Pipeline
IAM Setup:

Create user with EC2/ECR permissions

GitHub Secrets:

Copy
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
ECR_REPOSITORY_URL
EC2 Configuration:

Ubuntu instance

Docker installed

Docker Build
bash
Copy
docker build -t mlflow-model .
docker run -p 5000:5000 mlflow-model
💻 Technologies Used
Technology	Purpose
MLflow	Experiment tracking
DVC	Data versioning
Docker	Containerization
AWS EC2/ECR	Cloud deployment
GitHub Actions	CI/CD automation
Python	Core programming
📬 Contact Information
Zeeshan Malik
📧 malikzeeshan3.1417@gmail.com
🔗 LinkedIn
🐱 GitHub

🙏 Acknowledgments
Special thanks to:

MLflow & DVC teams

GitHub Actions developers

AWS for cloud infrastructure

Open-source community

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
