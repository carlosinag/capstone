from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='parent template'),
    path('login/', views.login, name='login html'),
]