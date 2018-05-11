"""Views for the *flister* Django app"""
import os

from django.http import Http404
from django.shortcuts import render


def flist(request, path):
    """Render the list of files/folders in *path* with links to folders"""
    path = '/' + path
    folders = []
    files = []

    try:
        contents = os.listdir(path)
    except FileNotFoundError:
        raise Http404(path)

    for item in contents:
        if item.startswith('.'):
            continue

        fullpath = os.path.join(path, item)
        if os.path.isdir(fullpath):
            folders.append(item)
        else:
            files.append(item)

    folders.sort()
    files.sort()

    context = {'path': path, 'folders': folders, 'files': files}

    return render(request, 'listing.html', context)
