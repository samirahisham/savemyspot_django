The purpose of this project is to provide a queuing functionality to what is essentially a restaurant list app. You have been provided with a semi-built Django project as a starter file. We will be filling in the missing information together. 

For now go ahead and set up your environment.

```
virtualenv -python==python3 savemyspot_env
```

Once you create your virtual environment, go ahead and activate it, and clone [this repo](https://github.com/nalmutairi/savemyspot_django).

Make sure you install the requirements, that include: Django, Django restframework, jwt, pillow

```
pip install -r requirments.txt
```

Before starting, apply the migrations by running the following commands
```
python manage.py makemigrations

python manage.py migrate
```

To also have access to the admin page, create a super user for yourself and provide the necessary credentials (username and password)

```
python manage.py createsuperuser
```

Run the server to get a better idea of the data that we have and the type of data we need to acquire- mainly the queue information.

```
python manage.py runserver
```

Visit your localhost address at http://127.0.0.1:8000.
And browse the admin panel.

You will notice a few of my most visited Boston based restaurants are already there for you along with their menu items. Just a heads up that they aren’t necessarily implementing the queuing functionality as part of their customer experience, so if you find yourself drooling over their menu items you might find yourself waiting for the buzzer.



