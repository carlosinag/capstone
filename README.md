# Ultrasound Patient Management and Image Annotation

## Project Overview
This is a Django-based Ultrasound Patient Management and Image Annotation.

## Prerequisites
- Python 3.9+
- pip
- virtualenv (recommended)

## Setup and Installation

### 1. Clone the Repository and Install Dependencies
```bash
git clone https://github.com/carlosinag/capstone.git
cd capstone

# On Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

# Database Setup
python manage.py makemigrations
python manage.py migrate

# Create Superuser
python manage.py createsuperuser

# Run Development Server
python manage.py runserver
```

## Git Requirements
1. Clone Project
```bash
git clone (https://github.com/carlosinag/capstone.git)
```

2. Push Code
```bash
git add .
git commit -m "Message and Changes"
git push
```

3. Pull Project
```bash
git fetch
git pull
```

4. Create Branch
```bash
git branch <branch_name>
git checkout <branch_name>
