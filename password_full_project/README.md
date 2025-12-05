# Password Validator Project

## Overview
This project demonstrates a **secure, extensible password validation system** with a **ReactJS frontend** and a **Django backend**.  
It validates passwords against multiple rules and is designed for **future scalability**.

**Features:**
- Login page with ReactJS
- Server-side password validation
  - **Length check**
  - **Character check** (uppercase, digits, special characters)
  - **Blacklist check** (common/insecure passwords)
- Modular, plug-and-play validators
- Configuration-driven via `settings.py`
- Easily extendable for:
  - Online validation
  - Password history checks
  - Multi-factor authentication
  - Integration with external security APIs

---

## Getting Started

### Prerequisites

- Node.js and npm (for React frontend)
- Python 3.x
- Django 4.x
- Git

---

### Run Backend (Django)

1. Navigate to backend folder:

```bash
cd backend

Create and activate virtual environment:

python -m venv env
env\Scripts\activate      # Windows


##Install Django:

pip install django


##Run migrations (optional if using sqlite):

python manage.py migrate


##Start server:

python manage.py runserver


-->Backend API available at http://localhost:8000/api/login/

**##Run Frontend (React)**

Navigate to frontend folder:

cd frontend


##Install dependencies:

npm install


##Start React app:

npm start


-->Frontend will open at http://localhost:3000

###How It Works

User enters username and password in React login page.
Password is sent to Django backend via API call.
Backend runs all validators configured in settings.py.
If password passes all checks → login success.
Otherwise → error message returned.

##Extensibility

Add new validators by creating a new class in validators.py inheriting BaseValidator.

Enable/disable validators in settings.py:

PASSWORD_VALIDATORS = [
    "core.validators.LengthValidator",
    "core.validators.CharacterValidator",
    "core.validators.BlacklistValidator",
    "core.validators.YourNewValidator"
]


-->Validators are plug-and-play and reusable across projects.

###Future Enhancements

Multi-factor authentication integration
Password expiration policies
Online or API-based validation
Enhanced security logging





