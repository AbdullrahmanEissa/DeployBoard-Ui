# 🚀 DeployBoard

**DeployBoard** is a **production-minded full-stack deployment demo**.

This repository is **not about UI features** or application complexity.
It exists to demonstrate **how real systems are deployed, automated, and scaled** in practice.

The focus is on:

* Deployment architecture
* Infrastructure automation
* Clean separation of responsibilities
* Production-style workflows (without overengineering)

This project is intentionally **easy to understand**, even for non-technical reviewers.

---

## 🎯 What This Project Demonstrates

* Production-ready project structure
* Frontend build vs runtime separation
* Backend running behind a reverse proxy
* Clean Docker & Docker Compose setup
* Infrastructure as Code using Terraform
* Configuration management using Ansible
* Horizontal scaling behind a Load Balancer
* No hard-coded environments
* No Kubernetes, no buzzword inflation

This mirrors **real company setups**, simplified for clarity.

---

## 🧱 Architecture Overview (High Level)

```
User Browser
     |
     v
AWS Application Load Balancer
     |
     v
EC2 Instances (x5)
     |
     v
Nginx (Reverse Proxy)
     ├── /        → Frontend (Angular SPA – static files)
     └── /api     → Backend API (Flask)
                      |
                      v
                 Python Backend (internal only)
```

### Key Architecture Principles

* Users never talk directly to the backend
* Backend is never exposed publicly
* Nginx is the single entry point
* Frontend and backend are independent services
* Traffic is distributed across multiple EC2 instances

---

## 🛠 Technology Stack

### Frontend

* Angular
* Built once, served as static files
* Served using Nginx (no dev server)

### Backend

* Python (Flask)
* Gunicorn (production WSGI server)
* Internal service only

### Containerization

* Docker
* Docker Compose (v2)
* Internal Docker networking

### Infrastructure & Automation

* **Terraform** – infrastructure provisioning
* **Ansible** – server configuration & deployment
* **AWS EC2** – compute
* **AWS Application Load Balancer** – traffic distribution
* **Nginx** – reverse proxy

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
├── docker-compose/
│   └── docker-compose-prod.yml
│
├── terraform/
│   └── AWS infrastructure (EC2, ALB, SGs)
│
└── ansible/
    ├── inventory.ini
    ├── ansible.cfg
    └── deploy.yml
```

Each directory has **one clear responsibility**.

---

## 🏗 Terraform – Infrastructure Provisioning

Terraform is used to provision **all AWS infrastructure** in a repeatable way.

### What Terraform Creates

* 5 × EC2 instances (Ubuntu 22.04)
* Application Load Balancer (ALB)
* Target group with all EC2 instances registered
* Security groups for SSH and application traffic
* Consistent tagging and naming:

  ```
  server.1
  server.2
  server.3
  server.4
  server.5
  ```

### Terraform Responsibilities

* Infrastructure only
* No application logic
* No configuration steps

This separation keeps infrastructure **immutable and reproducible**.

---

## ⚙️ Ansible – Configuration & Deployment

Ansible is used **after Terraform** to configure the EC2 instances and deploy the application.

### What Ansible Does

On each EC2 instance:

1. Updates system packages
2. Installs Docker (if missing)
3. Installs Docker Compose v2 plugin
4. Ensures Docker service is running
5. Clones the application repository
6. Builds Docker images
7. Runs the application using Docker Compose

All tasks are **idempotent** and safe to re-run.

---

### Ansible Inventory (Example)

```ini
[deployboard]
server1 ansible_host=<ip>
server2 ansible_host=<ip>
server3 ansible_host=<ip>
server4 ansible_host=<ip>
server5 ansible_host=<ip>

[deployboard:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/project-key.pem
```

---

### Deployment Playbook

The main playbook (`deploy.yml`) performs a full deployment:

* Docker installation
* Docker Compose setup
* Repository cloning
* Image build
* Container startup

Docker Compose files live in:

```
/opt/deployboard/docker-compose/
```

Deployment is done with **one command**:

```bash
ansible-playbook deploy.yml
```

---

## ▶️ How the Application Runs

* Each EC2 instance runs:

  * Nginx
  * Frontend container
  * Backend container
* The Load Balancer distributes traffic across all instances
* Each instance is identical (stateless)

This enables:

* Horizontal scaling
* Fault tolerance
* Production-style traffic flow

---

## 🔐 Security & Production Notes

* Backend is not publicly exposed
* Only Nginx listens on public ports
* Services communicate over internal Docker networks
* No development servers in production
* No hard-coded credentials or environments

---

## 🧠 Why This Project Matters

Many demos stop at:

> “It works on my machine.”

DeployBoard shows:

* How infrastructure is provisioned
* How servers are configured automatically
* How applications are deployed consistently
* How systems scale behind a load balancer

This reflects **real DevOps / Platform Engineering work**, not toy examples.

---

## 👤 Intended Audience

* HR reviewers
* Technical recruiters
* Junior to mid-level DevOps hiring managers
* Engineers learning real deployment workflows

No deep framework knowledge is required to understand this project.

---

## ✅ Project Status

✔ Working
✔ Automated
✔ Scalable
✔ Production-minded
✔ Clean architecture

---

### Final Note

This repository focuses on **deployment quality and system design**, not application features.

That is intentional.
