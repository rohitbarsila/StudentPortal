from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import  routers
from .views import dataViewSet

router=routers.DefaultRouter()
router.register('data',dataViewSet)

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('query',views.query),
    path('login',views.login),
    path('dashboard',views.dashboard,),
    path('logout',views.logout),
]