flister
-------

A file browser written for Django.


To hack on flister:

```
$ django startproject filebrowser
$ pip install -e .
$ cd filebrowser
```

Then

    1. Edit `filebrowser/settings.py`
    2. Add `flister` to `INSTALLED_APPS`
    3. Change `ROOT_URLCONF` to `flister.urls`
