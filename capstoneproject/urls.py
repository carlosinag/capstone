from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('capstone.urls')),
    path('', include('accounts.urls')),
    path('', include('home.urls')),
]
