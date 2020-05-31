#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'asset'
urlpatterns = [
    path('update/', views.update, name='update'),
    path('', views.index, name='index')
]

