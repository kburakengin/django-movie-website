# movie-website-project - Django

  This is a simple django movie website project to improve my skills with Django.
 
## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/Kburak/django.git
$ cd django/catalog
```
##### Create the virtualenv and activate it
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

##### Or on Windows cmd::
```bash
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Create a Super User to access admin panel
```bash
$ python manage.py createsuperuser
```

##### Make Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

##### Run the app
```bash
$ python manage.py runserver
```