print("polls.urls is being imported")
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]