flister
-------

A file browser written for Django.


To hack on flister:

If this is your first time create a Python virtual environment

```
$ python3 -m venv flister
```

Activate your virtual enviroment

In Linux/Mac:

```
$ source flister/bin/activate
```

In Windows:

```
C:\> flister\Scripts\activate.bat
```

For more information on the Python **venv** tool:

https://docs.python.org/3/library/venv.html


Install *flister* in developer mode

```
$ pip install -e .
$ django startproject filebrowser
$ cd filebrowser
```

Then

1. Edit `filebrowser/settings.py`
2. Add `flister` to `INSTALLED_APPS`
3. Change `ROOT_URLCONF` to `flister.urls`

You should then be able to run `runserver`:

```
$ ./manage.py runserver
```

And you should be able to reach the site at http://127.0.0.1:8000/
