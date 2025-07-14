# 🚀 Assignment - FastAPI Deployment: Iris Classifier API

This project demonstrates how to **train a Machine Learning model** (Iris Classifier using Logistic Regression), **build a REST API** using **FastAPI**, and **deploy it using Docker**. This assignment was done as part of an AI Engineering Internship evaluation.

---

## 📌 Features

- Trained an ML model using the Iris dataset with `scikit-learn`
- Applied basic feature engineering (handling nulls, scaling)
- Built an API using **FastAPI** to serve model predictions
- Containerized the entire application using **Docker**
- ✅ Bonus: Published image on **Docker Hub** for public access

---

## 🧠 Model Details

- **Dataset**: Iris Flower Dataset
- **Algorithm**: Logistic Regression
- **Accuracy**: ~93%
- **Input**: Petal and sepal measurements
- **Output**: Predicted species








-

## ▶️ How to Run Locally

### 1. Clone the Repo


git clone https://github.com/sujithreddy0007/Assignment-FastAPI-Deployment
cd Assignment-FastAPI-Deployment
2. (Optional) Create Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate       # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run FastAPI App
bash
Copy
Edit
uvicorn app.main:app --reload
Open your browser at:
📍 http://localhost:8000/docs

🐳 Docker Setup
✅ Build Docker Image
bash
Copy
Edit
docker build -t fastapi-iris-app .
✅ Run Docker Container
bash
Copy
Edit
docker run -d -p 8000:8000 fastapi-iris-app
✅ Test API in Browser
bash
Copy
Edit
http://localhost:8000/docs
🌐 Docker Hub (Bonus)
You can run the app directly using my public Docker image:

bash
Copy
Edit
docker pull sujithreddy0007/fastapi-iris-app
docker run -d -p 8000:8000 sujithreddy0007/fastapi-iris-app

✍️ Author

Sujith Mani Kumar Reddy