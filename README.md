# Movie Store (Django Project)
<img width="511" height="231" alt="image" src="https://github.com/user-attachments/assets/1202a49c-f74d-4910-b421-1e7077f2899e" />


This is a simple movie store web app built with Django. It is based on a book project and follows standard MVC (Model-View-Template) structure.

## Features

* Display list of movies
* View movie details
* Add new movies
* Edit existing movies
* Delete movies
* Basic admin panel using Django admin

## Tech Stack

* Python
* Django Django
* HTML / CSS
* SQLite database

## Project Structure

* `models.py` – database structure for movies
* `views.py` – logic for pages
* `urls.py` – routing
* `templates/` – HTML pages
* `admin.py` – admin configuration

## How to Run

1. Install dependencies:

```bash
pip install django
```

2. Run migrations:

```bash
python manage.py migrate
```

3. Start server:

```bash
python manage.py runserver
```

4. Open in browser:

```
http://127.0.0.1:8000/
```

## What I Learned

* How Django projects are structured
* How models, views, and templates work together
* CRUD operations in Django
* Basic web app development

## Future Improvements

* Add user login system
* Add movie ratings and reviews
* Improve UI design
* Add search and filters
