# Smart University Management System (UMS)

A full-stack Django application designed to manage core university operations including admissions, academics, examinations, and finance. The system focuses on clean backend architecture, clear data relationships, and a practical user interface built with Django templates.

---

## Overview

The Smart University Management System (UMS) models real-world university workflows in a structured and maintainable way. It supports multiple user roles, academic processes, and financial tracking, making it suitable for managing day-to-day university operations in a centralized system.

---

## Key Features

### Role-Based Authentication

* Separate access for students, faculty, staff, and administrators
* Custom user model with profile support

### Admissions Management

* Capture student applications
* Track admission status changes
* Maintain a structured intake pipeline

### Course Management

* Manage course catalog
* Create academic terms and course offerings
* Handle student enrollments

### Exams and Results

* Schedule exams for course offerings
* Record and manage student exam results

### Finance Management

* Create fee invoices
* Record payments
* Track payment status

### Dashboards

* KPI tiles for high-level insights
* Recent activity overview for quick monitoring

### Administration

* Django admin configured for efficient data entry and management

---

## Tech Stack

* Python
* Django 4.2
* SQLite (used for development and demonstration)
* Django Templates
* Bootstrap 5

---

## Project Structure

```
accounts/        # Custom user model, roles, profiles, authentication
admissions/      # Admission applications and status tracking
courses/         # Courses, academic terms, offerings, enrollments
exams/           # Exams and results
finance/         # Fee invoices and payments
dashboard/       # KPI summaries and recent activity
templates/       # UI templates
static/          # CSS and static assets
manage.py
requirements.txt
README.md
```

---

## Getting Started

### Create and activate virtual environment (Windows PowerShell)

```
python -m venv .venv
.\venv\Scripts\Activate.ps1
```

### Install dependencies

```
pip install -r requirements.txt
```

### Apply migrations

```
python manage.py migrate
```

### Create admin user

```
python manage.py createsuperuser
```

### Run the development server

```
python manage.py runserver
```

---

## Access URLs

* Application:
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

* Admin Panel:
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Notes

* SQLite is used for simplicity and ease of setup.
* Django admin is used for managing core data efficiently.
* UI templates are kept clean and professional to support usability.

---

## Future Enhancements

* REST API layer for mobile or external integrations
* Attendance management system
* Timetable and scheduling module
* More granular role-based dashboards and permissions
* Integration with payment gateways or POS systems

---

## Author

**Muhammad Tayab Farooq**
Email: **[muhammadtayabfarooq@gmail.com](mailto:muhammadtayabfarooq@gmail.com)**
Backend Developer — Python & Django
Experience: **2+ years**

---
