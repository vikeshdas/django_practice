
from django.urls import path
from category.views import CategoryViews

urlpatterns = [
    path('/',CategoryViews.as_view())
]