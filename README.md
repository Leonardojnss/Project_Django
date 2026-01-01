# Django Project - REST API

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Django](https://img.shields.io/badge/django-6.0-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.16-red.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![AWS](https://img.shields.io/badge/AWS-deployed-orange.svg)

This is a Django REST API project that manages information about books, courses, and students.

## 📋 Description

The project consists of a RESTful API developed with Django and Django REST Framework, containing three main applications:

- **Books**: Book management
- **Courses**: Course management
- **Students**: Student management

## 🚀 Technologies Used

- Python 3.12
- Django 6.0
- Django REST Framework 3.16
- PostgreSQL 15
- Docker & Docker Compose
- Gunicorn (WSGI production server)
- WhiteNoise (static files)
- pytest (automated testing)
- drf-yasg (Swagger/OpenAPI documentation)
- JWT (JSON Web Token authentication)
- **AWS EC2** (production deployment)
- **GitHub Actions** (CI/CD)

---

## 🌐 Live Demo

**🎯 Production API (AWS):**

- 🔗 **Base URL:** http://13.222.230.178:8000
- 📚 **Swagger UI:** http://13.222.230.178:8000/swagger/
- 📖 **ReDoc:** http://13.222.230.178:8000/redoc/
- 🔐 **Admin Panel:** http://13.222.230.178:8000/admin/

**Test Credentials:**
```
Username: admin
Password: admin123
```

⚠️ **Note:** This is a demonstration environment. In real production, use secure credentials and HTTPS.

---

## 🐳 Running with Docker (RECOMMENDED)

### **Prerequisites:**
- Docker Desktop installed
- Git (optional)

### **1. Clone the repository:**
```bash
git clone https://github.com/Leonardojnss/Project_Django.git
cd project_django
```

### **2. Configure environment variables (optional):**

The project comes with default values in `docker-compose.yml`, but you can create a `.env` file:

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=django_password
DB_HOST=db
DB_PORT=5432
```

### **3. Build and start:**

```bash
# Build images
docker-compose build

# Start containers
docker-compose up

# Or start in background
docker-compose up -d
```

### **4. Create superuser:**

In another terminal:

```bash
docker-compose exec web python manage.py createsuperuser
```

### **5. Access:**

- **API:** http://localhost:8000/
- **Swagger:** http://localhost:8000/swagger/
- **ReDoc:** http://localhost:8000/redoc/
- **Admin:** http://localhost:8000/admin/

---

## 💻 Running Locally (without Docker)

### **Prerequisites:**
- Python 3.12+
- PostgreSQL 15+ installed and running

### **1. Create virtual environment:**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### **2. Install dependencies:**

```bash
pip install -r requirements.txt
```

### **3. Configure database:**

Create a PostgreSQL database:

```sql
CREATE DATABASE django_db;
CREATE USER django_user WITH PASSWORD 'django_password';
GRANT ALL PRIVILEGES ON DATABASE django_db TO django_user;
```

### **4. Create `.env` file:**

```env
DEBUG=True
SECRET_KEY=django-insecure-change-this-in-production
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=django_password
DB_HOST=localhost
DB_PORT=5432
```

### **5. Run migrations:**

```bash
python manage.py migrate
```

### **6. Create superuser:**

```bash
python manage.py createsuperuser
```

### **7. Start server:**

```bash
python manage.py runserver
```

---

## 🧪 Running Tests

### **With Docker:**

```bash
docker-compose exec web pytest
```

### **Locally:**

```bash
pytest
```

### **With coverage:**

```bash
pytest --cov=. --cov-report=html
```

---

## ☁️ Deployment (AWS EC2 + Docker)

### **🏗️ Deployment Architecture**

```
GitHub Repository (production branch)
         ↓
   GitHub Actions (CI/CD)
         ↓
   AWS EC2 Instance (Ubuntu 22.04)
         ↓
   Docker Compose
    ├── PostgreSQL 15 (database)
    └── Django + Gunicorn (web server)
```

---

### **📦 Deployment Prerequisites**

1. **AWS Account** with an EC2 instance (t2.micro for testing)
2. **Security Group** configured with:
   - Port 22 (SSH)
   - Port 8000 (API)
   - Port 80 (HTTP - optional)
   - Port 443 (HTTPS - optional)
3. **SSH key pair** (.pem file) to access the instance

---

### **🚀 Manual Deployment (Step by Step)**

#### **1. Connect to EC2:**

```bash
ssh -i your-key.pem ubuntu@YOUR_EC2_IP
```

#### **2. Install Docker:**

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
sudo apt install -y docker.io docker-compose

# Add user to docker group
sudo usermod -aG docker $USER

# Restart session
exit
# Reconnect via SSH
```

#### **3. Clone repository:**

```bash
git clone https://github.com/Leonardojnss/Project_Django.git
cd Project_Django
git checkout production
```

#### **4. Create `.env` file:**

```bash
nano .env
```

**Paste:**

```env
DEBUG=False
SECRET_KEY=django-insecure-CHANGE-THIS-IN-PRODUCTION
ALLOWED_HOSTS=YOUR_EC2_IP,your-domain.com,localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=SecurePassword@2025!
DB_HOST=db
DB_PORT=5432
```

**Save:** `Ctrl+O` → `Enter` → `Ctrl+X`

#### **5. Deploy:**

```bash
# Build images
docker compose -f docker-compose.prod.yml build

# Start containers in background
docker compose -f docker-compose.prod.yml up -d

# View logs in real-time
docker compose -f docker-compose.prod.yml logs -f
```

**Wait until you see:** `Application startup complete` or `Booting worker with pid`

**Press** `Ctrl+C` to exit logs.

#### **6. Verify:**

```bash
# Check running containers
docker compose -f docker-compose.prod.yml ps

# Test API locally on EC2
curl http://localhost:8000/swagger/
```

#### **7. Access from anywhere:**

Open in browser: `http://YOUR_EC2_IP:8000/swagger/`

---

### **⚙️ Automated Deployment (GitHub Actions - CI/CD)**

This project uses **CI/CD** with GitHub Actions. Every time you `git push` to the `production` branch, deployment happens **automatically**!

#### **📋 How it works:**

1. ✅ You **push** to the `production` branch
2. ✅ GitHub Actions **detects** the event
3. ✅ Workflow **connects** to EC2 via SSH
4. ✅ Performs **git pull** of updated code
5. ✅ **Rebuilds** Docker containers
6. ✅ **Restarts** the application
7. ✅ Complete deployment in **~2 minutes**! 🚀

#### **🔧 Configure GitHub Actions:**

**1. Add Secrets on GitHub:**

Go to: `Settings` → `Secrets and variables` → `Actions` → `New repository secret`

**Add 3 secrets:**

| Secret Name | Value |
|------------|-------|
| `EC2_HOST` | EC2 public IP (e.g., `13.222.230.178`) |
| `EC2_USERNAME` | `ubuntu` (or your SSH username) |
| `EC2_SSH_KEY` | **Complete** content of `.pem` file |

**2. Workflow is already configured in:**

`.github/workflows/deploy.yml`

**3. Test automated deployment:**

```bash
# Make any change
echo "# Test CI/CD" >> README.md

# Commit and push
git add .
git commit -m "test: trigger automated deploy"
git push origin production
```

**4. Monitor deployment:**

- Go to: `https://github.com/Leonardojnss/Project_Django/actions`
- Click on the running workflow
- View real-time logs

---

### **🔄 Useful Commands (EC2 Management)**

```bash
# View logs in real-time
docker compose -f docker-compose.prod.yml logs -f web

# Last 50 log lines
docker compose -f docker-compose.prod.yml logs --tail=50 web

# Restart only Django (without rebuild)
docker compose -f docker-compose.prod.yml restart web

# Stop all containers
docker compose -f docker-compose.prod.yml down

# Stop and remove volumes (⚠️ DELETES DATABASE!)
docker compose -f docker-compose.prod.yml down -v

# Update code and complete rebuild
git pull origin production
docker compose -f docker-compose.prod.yml up -d --build

# View resource usage (CPU, RAM)
docker stats

# Enter Django container
docker compose -f docker-compose.prod.yml exec web bash

# Create superuser (inside container)
docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

# Database backup
docker compose -f docker-compose.prod.yml exec db pg_dump -U django_user django_db > backup_$(date +%Y%m%d).sql

# Restore backup
docker compose -f docker-compose.prod.yml exec -T db psql -U django_user django_db < backup_20250101.sql
```

---

### **🔒 Security (Production Best Practices)**

#### **1. Change default credentials:**

```bash
# Connect to container
docker compose -f docker-compose.prod.yml exec web bash

# Create new secure superuser
python manage.py createsuperuser

# Optional: Delete test "admin" user
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.filter(username='admin').delete()
>>> exit()
```

#### **2. Use HTTPS (SSL/TLS):**

- Configure **Nginx** as reverse proxy
- Use **Let's Encrypt** (Certbot) for free certificate
- Or use **AWS Load Balancer** with ACM certificate

#### **3. Restrict SSH access in Security Group:**

```
Type: SSH
Port: 22
Source: YOUR_PUBLIC_IP/32  ← Only your IP!
Description: SSH from my IP only
```

#### **4. Protect environment variables:**

- **Never** commit `.env` files to Git
- Use **AWS Secrets Manager** or **Parameter Store**
- Rotate `SECRET_KEY` periodically

#### **5. Configure firewall (UFW):**

```bash
sudo ufw enable
sudo ufw allow 22/tcp      # SSH
sudo ufw allow 8000/tcp    # API
sudo ufw status
```

---

### **📊 Monitoring**

#### **Logs:**

```bash
# Django logs
docker compose -f docker-compose.prod.yml logs -f web

# PostgreSQL logs
docker compose -f docker-compose.prod.yml logs -f db

# View errors (last 24h)
docker compose -f docker-compose.prod.yml logs --since 24h web | grep ERROR
```

#### **Performance Metrics:**

```bash
# Real-time CPU, Memory, Network
docker stats

# Disk space
df -h

# Container status
docker compose -f docker-compose.prod.yml ps

# Health check
curl -I http://localhost:8000/admin/
```

---

### **🆘 Troubleshooting**

#### **❌ Container won't start:**

```bash
# View complete logs
docker compose -f docker-compose.prod.yml logs web

# Check environment variables
docker compose -f docker-compose.prod.yml config
```

#### **❌ Database connection error:**

```bash
# View PostgreSQL logs
docker compose -f docker-compose.prod.yml logs db

# Test manual connection
docker compose -f docker-compose.prod.yml exec db psql -U django_user -d django_db

# Check if container is running
docker ps | grep postgres
```

#### **❌ API returns 500 error:**

```bash
# View detailed Django logs
docker compose -f docker-compose.prod.yml logs -f web

# Verify DEBUG is False
cat .env | grep DEBUG

# Enter container and test manually
docker compose -f docker-compose.prod.yml exec web python manage.py check
```

#### **❌ GitHub Actions deployment fails:**

```bash
# Verify SSH is accessible
ssh -i your-key.pem ubuntu@YOUR_EC2_IP

# Check secrets on GitHub
# Settings → Secrets → Actions

# Test SSH connection with verbose
ssh -v -i your-key.pem ubuntu@YOUR_EC2_IP
```

---

## 📚 API Endpoints

### **Authentication:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Obtain JWT token |
| POST | `/api/token/refresh/` | Refresh token |

### **Students:**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/students/` | List students | ✅ Yes |
| POST | `/students/` | Create student | ✅ Yes |
| GET | `/students/{id}/` | Student details | ✅ Yes |
| PUT | `/students/{id}/` | Update student | ✅ Yes |
| DELETE | `/students/{id}/` | Delete student | ✅ Yes |

### **Courses:**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/courses/` | List courses | ✅ Yes |
| POST | `/courses/` | Create course | ✅ Yes |
| GET | `/courses/{id}/` | Course details | ✅ Yes |
| PUT | `/courses/{id}/` | Update course | ✅ Yes |
| DELETE | `/courses/{id}/` | Delete course | ✅ Yes |

### **Books:**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/books/` | List books | ✅ Yes |
| POST | `/books/` | Create book | ✅ Yes |
| GET | `/books/{id}/` | Book details | ✅ Yes |
| PUT | `/books/{id}/` | Update book | ✅ Yes |
| DELETE | `/books/{id}/` | Delete book | ✅ Yes |

---

## 🔐 Authentication

The API uses **JWT (JSON Web Token)**. To access protected endpoints:

### **1. Get token:**

```bash
curl -X POST http://13.222.230.178:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### **2. Use token in requests:**

```bash
curl -X GET http://13.222.230.178:8000/students/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

### **3. Or use Swagger UI:**

1. Go to http://13.222.230.178:8000/swagger/
2. Click **"Authorize"** (green button)
3. Paste the **access token** (without "Bearer")
4. Click **"Authorize"** → **"Close"**
5. Now you can test all endpoints! 🎉

---

## 🐳 Useful Docker Commands

```bash
# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Stop and remove volumes (WARNING: deletes database data)
docker-compose down -v

# Enter Django container
docker-compose exec web bash

# Run migrations
docker-compose exec web python manage.py migrate

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# View running containers
docker ps

# Remove all unused images
docker system prune -a
```

---

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is under the MIT license. See the `LICENSE` file for more details.

---

## 👨‍💻 Author

**Leonardo José** - Backend Python/Django Developer

- 📧 Email: leonardojosenogueiradossantoss@gmail.com
- 🐙 GitHub: [@Leonardojnss](https://github.com/Leonardojnss)
- 🔗 Project: [Project_Django](https://github.com/Leonardojnss/Project_Django)
- 🌐 **Live API:** http://13.222.230.178:8000/swagger/

---

## 🎓 What I Learned

This project covers:

### **Backend & API:**
- ✅ REST API architecture and best practices
- ✅ Django REST Framework (viewsets, serializers)
- ✅ Authentication and authorization (JWT)
- ✅ Data validation and serialization
- ✅ API documentation (Swagger/OpenAPI)

### **Database:**
- ✅ PostgreSQL database design
- ✅ Django ORM (models, migrations)
- ✅ Database relationships (ForeignKey, ManyToMany)

### **DevOps & Deployment:**
- ✅ Docker containerization
- ✅ Docker Compose orchestration
- ✅ AWS EC2 deployment
- ✅ CI/CD with GitHub Actions
- ✅ Production environment configuration
- ✅ Security best practices

### **Testing:**
- ✅ Unit testing with pytest
- ✅ Integration testing
- ✅ Test coverage analysis

---

**⭐ If this project helped you, please leave a star on GitHub!**

**Made with ❤️ and Python by Leonardo José**