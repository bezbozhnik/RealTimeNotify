from django.urls import path, include
from . import views

urlpatterns = [
    # Другие URL-маршруты вашего проекта
    path('', views.index, name='index'),
]