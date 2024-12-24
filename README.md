#  QuiraQuest Daytona

![License](https://img.shields.io/github/license/Karush2807/lafda-centre?style=flat-square)  
![Last Commit](https://img.shields.io/github/last-commit/Karush2807/lafda-centre?style=flat-square)  
![Issues](https://img.shields.io/github/issues/Karush2807/lafda-centre?style=flat-square)

**Lafda Centre** is a Django-based platform designed to manage and streamline dispute resolution processes efficiently. This project aims to serve as a centralized hub for managing cases, tracking their status, and improving communication between involved parties.

## 🚀 Features

- **Case Management**: Create, update, and track the status of cases.  
- **Role-Based Access**: Different dashboards for administrators, moderators, and users.  
- **Notifications System**: Notify users about case updates and deadlines.  
- **Data Analytics**: Gain insights through visual analytics on resolved cases and pending issues.  
- **Scalable Architecture**: Built with Django to ensure scalability and ease of deployment.

## 🛠️ Tech Stack

- **Backend**: Django, Django Rest Framework  
- **Frontend**: HTML, CSS, Bootstrap (or other frontend library if used)  
- **Database**: SQLite (default), with support for PostgreSQL/MySQL  
- **Other**: Celery for task scheduling, Redis for caching and message brokering (if used)

## 📂 Directory Structure

```plaintext
lafda-centre/
├── lafda_centre/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── cases/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
├── templates/
│   ├── base.html
│   ├── dashboard.html
├── manage.py
└── README.md
```

## Setup Instrucitons

1. Clone the repository
```bash
git clone https://github.com/Karush2807/lafda-centre.git
```

2. Navigate to the project directory:
```bash
cd lafda-centre
```

3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate 
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/Karush2807/lafda-centre/issues).

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature/YourFeatureName
    ```


