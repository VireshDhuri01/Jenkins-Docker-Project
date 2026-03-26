# 🚀 DevOps Task Manager

A full-stack DevOps project demonstrating containerization, orchestration, and CI/CD using Docker and Jenkins. This project implements a 2-tier architecture with a Flask-based frontend and a MySQL backend.

---

## 📌 Features

- 🐍 Flask-based web application (frontend)
- 🐬 MySQL database (backend)
- 🐳 Dockerized services
- 📦 Docker Compose for multi-container orchestration
- ⚙️ Jenkins CI/CD pipeline integration
- ☁️ Deployed on AWS EC2

---

## 🧱 Architecture

```
User → Flask App → MySQL Database
```

- Frontend handles UI and API requests
- Backend stores and manages task data

---

## 📁 Project Structure

```
devops-task-manager/
│
├── docker-compose.yml
├── requirements.txt
│
├── frontend/
│   ├── Dockerfile
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── backend/
│   └── init.sql
│
└── Jenkinsfile
```

---

## ⚙️ Technologies Used

- Python (Flask)
- MySQL
- Docker
- Docker Compose
- Jenkins
- AWS EC2

---

## 🚀 Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd devops-task-manager
```

### 2. Run Using Docker Compose

```
docker compose up -d
```

### 3. Access Application

```
http://<EC2-PUBLIC-IP>:5000
```

---

## 🔁 CI/CD Pipeline (Jenkins)

The Jenkins pipeline automates:

- Cloning repository from GitHub
- Building Docker images
- Running containers using Docker Compose
- Verifying running services

### Sample Pipeline Stages

- Clone Repo
- Build Containers
- Deploy Application
- Verify Deployment

---

## 🐳 Docker Details

### Services:

- **frontend** → Flask App
- **mysql** → Database

### Networking:

- Custom Docker network for service communication

---

## ⚠️ Challenges Faced

- Docker permission issues with Jenkins user
- MySQL container initialization delays
- Resource limitations on t3.micro EC2 instance

---

## 💡 Learnings

- Hands-on experience with Docker networking
- CI/CD pipeline creation using Jenkins
- Debugging real-world DevOps issues
- Cloud deployment on AWS EC2

---

## 🔥 Future Improvements

- Add Nginx reverse proxy
- Enable HTTPS (SSL)
- Deploy using Kubernetes
- Push images to Docker Hub

---

## 🙌 Author

**Viresh Dhuri**

---

## ⭐ Acknowledgment

This project was built as part of hands-on DevOps learning and practice.

