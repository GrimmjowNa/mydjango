from django.urls import include, path
from .views import Home
from .sub1 import urls as sub1_urls

urlpatterns = [
    path('', Home.as_view()),
    path('sub1', include(sub1_urls)),
]