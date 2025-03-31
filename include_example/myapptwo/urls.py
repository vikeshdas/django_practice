from django.urls import path
from myapptwo import views

urlpatterns = [
    path('', views.index,name='index'),
]