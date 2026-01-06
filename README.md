# 🚀 DeployBoard

**DeployBoard** is a simple, production-style **full-stack deployment demo**.

This project is **not about features or UI**.
It exists to demonstrate **real-world deployment thinking**:

* How frontend and backend are separated
* How production builds work
* How services communicate securely
* How Docker and Nginx are used correctly

It is intentionally **easy to understand**, even for non-technical readers.

---

## 🎯 What This Project Demonstrates

* Production-ready project structure
* Frontend build vs runtime separation
* Backend running behind a reverse proxy
* Clean Docker & Docker Compose setup
* No hard-coded environments
* No over-engineering

This is the kind of setup used in **real companies**, just simplified.

---

## 🧱 Architecture Overview (Simple)

```
Browser
   ↓
Nginx (Frontend Container)
   ├── /        → Angular SPA (static files)
   └── /api     → Backend API (Flask)
                    ↓
               Python Backend (internal only)
```

### Key Ideas

* Users **only talk to Nginx**
* Backend is **never exposed publicly**
* Frontend and backend are **independent services**

---

## 🛠 Technology Stack

### Frontend

* Angular
* Built once, served as static files
* Served using **Nginx**

### Backend

* Python (Flask)
* Runs using **Gunicorn** (production server)
* Internal service only

### Infrastructure

* Docker
* Docker Compose
* Internal Docker networking

---

## 📁 Project Structure

```
DeployBoard/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   └── deployboard-ui/
│       ├── Dockerfile
│       ├── nginx.conf
│       └── Angular source code
│
└── docker-compose/
    └── docker-compose-prod.yml
```

Each part has **one responsibility only**.

---

## ▶️ How to Run the Project (Step-by-Step)

### Requirements

* Docker
* Docker Compose

No other setup is needed.

---

### Step 1: Go to the docker-compose folder

```bash
cd docker-compose
```

---

### Step 2: Build and run everything

```bash
docker compose -f docker-compose-prod.yml up --build
```

Docker will:

* Build the backend image
* Build the frontend image
* Start both services
* Connect them automatically

---

### Step 3: Open the application

Open your browser:

```
http://localhost
```

You should see the frontend running.

---

### Step 4: Test the backend (optional)

Open:

```
http://localhost/api/status
```

This confirms:

* Backend is running
* Nginx is proxying correctly

---

## 🔐 Security & Production Notes

* Backend is **not exposed to the internet**
* Only Nginx has a public port
* Services communicate over an internal network
* No development servers are used in production

---

## 🧠 Why This Project Matters

Many demos show only:

> "It works on my machine"

DeployBoard shows:

* How applications are **actually deployed**
* How environments are separated
* How infrastructure decisions are made

This reflects **real DevOps / Platform engineering work**.

---

## 👤 Intended Audience

* HR reviewers
* Technical recruiters
* Junior-to-mid DevOps hiring managers

No deep framework knowledge is required to understand this project.

---

## ✅ Status

✔ Working
✔ Production-style
✔ Clean architecture

---

**Thank you for reviewing this project.**

This repository focuses on **deployment quality**, not application features.
