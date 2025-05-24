Mini To-Do List Web App
A Django web application for managing personal tasks, with user authentication to ensure tasks are private to each user.
Features

User registration, login, and logout using Django's authentication system.
Add tasks with a title and optional description.
View tasks with creation date and completion status.
Mark tasks as completed or undone with strikethrough styling.
Edit task title and description.
Delete tasks.
Tasks restricted to the logged-in user for privacy.
Responsive UI with custom CSS and emoji-based buttons.

Tech Stack

Backend: Django, SQLite
Frontend: HTML, CSS (static/css/styles.css)
Tools: Python, VS Code

Setup

Create a virtual environment: python -m venv venv
Activate the virtual environment:
Linux/Mac: source venv/bin/activate
Windows: venv\Scripts\activate


Install dependencies: pip install django
Apply migrations: python manage.py migrate
Run the server: python manage.py runserver
Visit: http://127.0.0.1:8000

Usage

Sign up at /accounts/signup/ to create an account.
Log in at /accounts/login/ to access your task list.
Add, edit, toggle, or delete tasks from the task list.
Log out to secure your session.


