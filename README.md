Django Contact Book

A modern contact management app built with Django. Allows you to add, view, edit, and delete contacts with a clean, responsive UI using Bootstrap 5 and Font Awesome icons.

🔹 Features

Add, edit, delete, and view contacts

Responsive card-based UI

Sidebar navigation + floating add button

Admin panel integration

⚙ Setup

Clone the repo:

git clone <repo-url>
cd <project-folder>


Create a virtual environment & activate:

python3 -m venv venv
source venv/bin/activate   # macOS/Linux


Install Django:

pip install django


Run migrations:

python manage.py makemigrations
python manage.py migrate


Start server:

python manage.py runserver


Visit http://127.0.0.1:8000/ to use the app.

📂 Tech Stack

Backend: Django, Python

Frontend: HTML, CSS, Bootstrap, Font Awesome

Database: SQLite

💡 Notes

Use correct template names in {% extends %}

Ensure URL names match in {% url 'name' %}

Frontend updates reflect backend database via Django views
