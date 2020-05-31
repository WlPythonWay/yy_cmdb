#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
]

