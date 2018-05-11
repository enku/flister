"""Urlconf for flister"""
from django.urls import path

import flister.views


urlpatterns = [
    path('<path:path>/', flister.views.flist),
]
