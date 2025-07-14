# 🧠 Assignment - FastAPI Deployment: Iris Classifier API

This project is part of an **AI Engineering Internship Assignment** and demonstrates the **deployment of a machine learning model** using **FastAPI** and **Docker**.

---

## 🌟 Features

✅ Trained a Logistic Regression model on the Iris Dataset  
✅ Performed preprocessing including null value handling and scaling  
✅ Developed a FastAPI REST API for real-time predictions  
✅ Containerized the application using Docker  
✅ Bonus: Can be pulled and run from Docker Hub


---
## 🧰 Tech Stack

| Layer                 | Technology Used                   | Purpose                                      |
|----------------------|-----------------------------------|----------------------------------------------|
| Language             | Python 3.10+                      | Core programming language                    |
| Libraries            | scikit-learn, pandas, numpy       | Model training and data preprocessing        |
| Model Serialization  | joblib                            | Saving and loading model & scaler            |
| API Framework        | FastAPI                           | Building RESTful API                         |
| Validation           | Pydantic                          | Input data validation for API                |
| Server               | Uvicorn                           | ASGI server to run FastAPI app               |
| Virtual Env          | venv                              | Isolated Python environment                  |
| Containerization     | Docker                            | Packaging app into portable container        |
| Documentation        | Swagger UI (via FastAPI)          | Interactive API documentation and testing    |
| IDE                  | Visual Studio Code (VS Code)      | Development and code editing                 |
| Version Control      | Git + GitHub                      | Source code management and collaboration     |

---
---

## 📁 Project Structure

```
Assignment-FastAPI-Deployment/
├── app/
│ ├── main.py # FastAPI application
│ ├── schema.py # Pydantic model for input validation
│ ├── model.pkl # Trained ML model
│ └── scaler.pkl # Scaler used for preprocessing
├── train/
│ └── train_model_assignment.ipynb # Jupyter notebook to train and save model
├── Dockerfile # Docker instructions
├── requirements.txt # Python dependencies
├── .gitignore # Git ignored files
├── .dockerignore # Docker ignored files
└── README.md # Documentation
```
---

## ⚙️ Getting Started

### ✅ Clone the Repository

```bash
git clone https://github.com/sujithreddy0007/Assignment-FastAPI-Deployment.git
cd Assignment-FastAPI-Deployment
```
---
### ✅ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```
---
---
### ✅ Install Dependencies
```bash
pip install -r requirements.txt

```
---
### The notebook performs:

Null handling

Scaling

Model training using Logistic Regression

Saving model.pkl and scaler.pkl in the app/ folder

---
---
### 🚀 Run the FastAPI App

```bash
uvicorn app.main:app --reload

Visit Swagger UI (Interactive API Docs):

http://127.0.0.1:8000/docs


```
---
---
---
### 🧪 Sample API Requests

🔹 GET /

Returns:

json
Copy
Edit
{
  "message": "Welcome to the Iris Classifier API"
}

🔹 POST /predict

```bash
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

```
Response:
```bash
{
  "prediction": "setosa"
}
```
---
### 🐳 Docker Deployment
✅ Build Docker Image
```bash
docker build -t fastapi-iris-app .
```
✅ Run Docker Container
```bash
docker run -d -p 8000:8000 fastapi-iris-app

```
---
### ✅ Share via Docker Hub
✅ Tag and Push Image
```bash
docker tag fastapi-iris-app yourdockerhubusername/fastapi-iris-app
docker push yourdockerhubusername/fastapi-iris-app
```
✅ Anyone Can Pull and Run
```bash
docker pull yourdockerhubusername/fastapi-iris-app
docker run -d -p 8000:8000 yourdockerhubusername/fastapi-iris-app

```
---
---
### 📊 Model Accuracy

| Metic             | Value                                  |
| -------------------- | -------------------------------------------- |
| Accuracy                             |93%
| Model | Logistic Regression|
| DataSet             | Iris Dataset (sklearn)                       |


---

### 🧠 Concepts Covered
Machine Learning Model Training & Preprocessing

API Development using FastAPI

Input validation using Pydantic Schemas

Dockerization of ML Service

Serialization of Model & Scaler using joblib

---
---
### 📄 Summary
This project shows how to train, build, and deploy a machine learning model using FastAPI and Docker. It covers data preprocessing, model training, API design, and containerization — making it suitable for production-level microservice deployments.

---
---
### 👨‍💻 Author
Sujith Mani Kumar Reddy

