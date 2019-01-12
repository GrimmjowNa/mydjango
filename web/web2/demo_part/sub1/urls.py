from django.urls import path
from .views import Home
from django.urls import include, path

urlpatterns = [
    path('', Home.as_view()),
]