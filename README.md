# 🚀 End-to-End ML Pipeline with MLflow & DVC

![MLflow](https://img.shields.io/badge/MLflow-%23FF6F00.svg?style=for-the-badge&logo=mlflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-%2395C93D.svg?style=for-the-badge&logo=dvc&logoColor=white)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 Overview
A production-ready machine learning pipeline featuring:
- **Experiment tracking** with MLflow
- **Data versioning** with DVC
- **CI/CD automation** via GitHub Actions
- **Cloud deployment** on AWS (EC2/ECR)
- **Containerization** with Docker

```mermaid
graph TD
    A[Raw Data] --> B[DVC Versioning]
    B --> C[Feature Engineering]
    C --> D[MLflow Tracking]
    D --> E[Model Training]
    E --> F[Model Registry]
    F --> G[Docker Packaging]
    G --> H[AWS Deployment]
🛠️ Quick Start
Prerequisites
Python 3.10+

Conda/Miniconda

Git

Docker (for containerization)

Installation
bash
Copy
# Clone repository
git clone https://github.com/tiksharsh/mlflow-project.git
cd mlflow-project

# Create conda environment
conda create -n mlproj python=3.10.9 -y
conda activate mlproj

# Install dependencies
pip install -r requirements.txt
Running the Pipeline
bash
Copy
# Start MLflow tracking server
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0

# Run main pipeline (in another terminal)
python src/main.py
🔍 MLflow Integration
Track experiments with:

python
Copy
import mlflow

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
Access the UI:

bash
Copy
mlflow ui --port 5000
Note: UI available at http://localhost:5000

🔄 DVC Workflow
bash
Copy
# Initialize DVC
dvc init

# Add data files
dvc add data/raw_dataset.csv

# Configure remote storage (AWS S3 example)
dvc remote add -d myremote s3://mybucket/dvc-storage

# Version data
dvc push
🚀 Deployment
AWS CI/CD Pipeline
Set up IAM user with EC2/ECR permissions

Configure GitHub Secrets:

Copy
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
ECR_REPOSITORY_URL
Push to trigger GitHub Actions workflow

Docker Build
bash
Copy
docker build -t mlflow-model .
docker run -p 5000:5000 mlflow-model
🧩 Project Structure
Copy
.
├── data/               # DVC-tracked datasets
├── src/
│   ├── main.py         # Pipeline entry point
│   ├── preprocessing/  # Feature engineering
│   └── models/         # Training scripts
├── mlruns/             # MLflow experiments
├── .github/
│   └── workflows/      # CI/CD pipelines
├── Dockerfile          # Container configuration
└── requirements.txt    # Python dependencies
🤝 Contributing
Fork the repository

Create your feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
Zeeshan Malik
📧 malikzeeshan3.1417@gmail.com
🔗 LinkedIn
🐱 GitHub
