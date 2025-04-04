# **E2E-ML-Project-with-MLflow & DVC**  

## Project Overview

**E2E-ML-Project-with-MLflow & DVC** is a comprehensive end-to-end machine learning pipeline built to demonstrate the full lifecycle of machine learning projects, including model training, tracking, versioning, and deployment. The project leverages **MLflow** for experiment tracking and **DVC** (Data Version Control) for managing datasets and model versions. This project provides a seamless workflow for data scientists and machine learning engineers to track their experiments, train models, and deploy them in production environments.

### Key Features:
- **Experiment Tracking** with MLflow.
- **Data Versioning and Model Management** with DVC.
- **CI/CD Pipeline** integrated with **GitHub Actions** and **AWS** for deployment.
- **Dockerized Environment** for easy reproduction of the machine learning pipeline.
- Integration with **Dagshub** for remote experiment tracking and collaboration.

---

## Table of Contents
- [Project Setup](#project-setup)
- [How to Run](#how-to-run)
- [MLflow Integration](#mlflow-integration)
- [DVC Integration](#dvc-integration)
- [Deployment Instructions](#deployment-instructions)
- [Technologies Used](#technologies-used)
- [Contact Information](#contact-information)
- [Acknowledgments](#acknowledgments)

---

## Project Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/tiksharsh/mlflow-project.git
cd mlflow-project
Step 2: Create a Conda environment
bash
Copy
Edit
conda create -n mlproj-venv python=3.10.9 -y
conda activate mlproj
Step 3: Install the required dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the application
bash
Copy
Edit
python app.py
Now, open your browser and go to localhost:5000 (or the port specified) to view the application.

How to Use MLflow
MLflow is used to track your machine learning experiments, manage models, and store artifacts. You can run MLflow UI to visualize the experiments.

To run MLflow UI:
bash
Copy
Edit
mlflow ui
The UI will be available at http://localhost:5000.

DVC Integration
DVC (Data Version Control) allows versioning of large datasets and model files efficiently. This project uses DVC to manage and version control the datasets and models in the pipeline.

How to use DVC:
Install DVC:

bash
Copy
Edit
pip install dvc
Initialize DVC:

bash
Copy
Edit
dvc init
To push data to remote storage (e.g., AWS S3, Google Cloud):

bash
Copy
Edit
dvc push
Deployment Instructions
CI/CD with GitHub Actions and AWS
This project integrates with GitHub Actions to automate the CI/CD pipeline and deploy the model using AWS EC2 and ECR (Elastic Container Registry).

Login to AWS Console and create an IAM user for deployment with the necessary access to EC2 and ECR.

Create an ECR repository to store the Docker image and push the model image to it.

Configure EC2 instance (Ubuntu) and install Docker.

Set up GitHub Actions for CI/CD.

For detailed instructions on setting up the CI/CD pipeline, check the AWS-CICD-Deployment-with-Github-Actions section.

Technologies Used
MLflow: For experiment tracking and model management.

DVC: For versioning data and models.

Docker: For containerizing the application.

AWS EC2 & ECR: For hosting and deploying the machine learning model.

GitHub Actions: For automating deployment.

Python: The primary programming language for developing the pipeline.

Contact Information
Feel free to reach out to me if you have any questions or are interested in collaborating on machine learning or AI projects.

Email: malikzeeshan3.1417@gmail.com

LinkedIn: @muhammadzeeshan007

GitHub: MalikZeeshan1122

Acknowledgments
Special thanks to the open-source community for providing the tools used in this project, including MLflow, DVC, GitHub Actions, and AWS. These tools enable us to manage machine learning models efficiently, automate workflows, and deploy models at scale.

License
This project is licensed under the MIT License - see the LICENSE file for details.
