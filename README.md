# Django Project - REST API

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Django](https://img.shields.io/badge/django-6.0-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.16-red.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-15-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

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

## 📚 API Endpoints

### **Authentication:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Obtain JWT token |
| POST | `/api/token/refresh/` | Refresh token |

### **Students:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students/` | List students |
| POST | `/students/` | Create student |
| GET | `/students/{id}/` | Student details |
| PUT | `/students/{id}/` | Update student |
| DELETE | `/students/{id}/` | Delete student |

### **Courses:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/courses/` | List courses |
| POST | `/courses/` | Create course |
| GET | `/courses/{id}/` | Course details |
| PUT | `/courses/{id}/` | Update course |
| DELETE | `/courses/{id}/` | Delete course |

### **Books:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | List books |
| POST | `/books/` | Create book |
| GET | `/books/{id}/` | Book details |
| PUT | `/books/{id}/` | Update book |
| DELETE | `/books/{id}/` | Delete book |

---

## 🔐 Authentication

The API uses JWT (JSON Web Token). To access protected endpoints:

### **1. Get token:**

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
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
curl -X GET http://localhost:8000/students/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

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
```

---

## 📁 Project Structure

```
project_django/
├── setup/                  # Django settings
│   ├── settings.py         # Main settings
│   ├── urls.py             # Main routes
│   └── wsgi.py             # WSGI for production
├── students/               # Students app
│   ├── models.py           # Student model
│   ├── serializers.py      # Student serializer
│   ├── views.py            # Student viewset
│   └── tests/              # Tests
├── courses/                # Courses app
├── books/                  # Books app
├── scripts/                # Utility scripts
│   └── start.sh            # Docker startup script
├── Dockerfile              # Docker image
├── docker-compose.yml      # Container orchestration
├── docker-compose.prod.yml # Production config
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables example
├── .env.production         # Production env template
├── .dockerignore           # Docker ignored files
├── .gitignore              # Git ignored files
├── pytest.ini              # Pytest configuration
└── README.md               # This file
```

---

## 🔧 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | `False` | Debug mode (True/False) |
| `SECRET_KEY` | - | Django secret key |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Allowed hosts |
| `DB_ENGINE` | `postgresql` | Database engine |
| `DB_NAME` | `django_db` | Database name |
| `DB_USER` | `django_user` | Database user |
| `DB_PASSWORD` | `django_password` | Database password |
| `DB_HOST` | `localhost` | Database host |
| `DB_PORT` | `5432` | Database port |

---

## 🤝 Contributing

1. Fork the project
2. Create a branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

This project is under the MIT license.

---

## 👨‍💻 Author

**Leonardo Jose** - Django REST API Developer

- 📧 Email: your-email@example.com
- 🐙 GitHub: [@your-username](https://github.com/your-username)
- 💼 LinkedIn: [your-profile](https://linkedin.com/in/your-profile)

---

## 🎓 What I Learned

This project covers:
- ✅ REST API architecture
- ✅ Authentication and authorization (JWT)
- ✅ Data serialization
- ✅ Automated testing
- ✅ Application containerization (Docker)
- ✅ Deployment and production
- ✅ Django best practices
- ✅ API documentation (Swagger)

---

**Made with ❤️ and Python**