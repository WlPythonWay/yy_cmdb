#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls.conf import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.cmdb_login, name="login"),
    path('logout/', views.cmdb_logout, name="logout"),
    path('my-page/', views.my_page, name="my-page"),
    path('manager/', views.user_manager, name="manager"),
    path('add/', views.add_user, name="add"),
    path('', views.test, name="test"),
]
