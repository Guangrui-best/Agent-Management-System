# Agent Management System

## Main Features

- Each agent (user) has information including username, email and unique id

- It supports CRUD

- It supports pagination

- It supports searching by conditions. e.g. Search by agents' username

- Each time when a user completes a successful registration, an email will be sent automatically to the user's registered email

## How to set up the project to run on your local machine?

#### Download the code to your PC, unpack the zip and move inside the folder.

#### Create a new Python Virtual Environment:
```
python3 -m venv venv
```

#### Activate the environment and install all the Python/Django dependencies:

```
source ./venv/bin/activate
pip install django
pip install djangorestframework
pip install django-rest-auth
pip install django-allauth
pip install django-registration
pip install django-crispy-forms
pip install requests
pip install pillow
pip install -m ./requirements.txt
```

#### Run migrations is essential to Django
```
python manage.py makemigrations
python manage.py migrate
```

#### Create a superuser is helpful to review all the users' information
```
python manage.py createsuperuser
```

## Notice before run the project

- In the ./AgentManagement/settings.py, you should firstly input your own email address and password at the **EMAIL_HOST_USER** and **EMAIL_HOST_PASSWORD** and figure out your email's host and port, which should be input at **EMAIL_HOST** and **EMAIL_PORT**.

- You can adjust the page size by changing the **PAGE_SIZE** in the **REST_FRAMEWORK** at ./AgentManagement/settings.py.

- You need to start debugging using Python: Django

- The available website is shown as below

    - http://127.0.0.1:8000

    - http://127.0.0.1:8000/admin/

    - http://127.0.0.1:8000/api/user/

    - http://127.0.0.1:8000/api/user/<int:pk>/

    - http://127.0.0.1:8000/accounts/register/

    - http://127.0.0.1:8000/accounts/login/
