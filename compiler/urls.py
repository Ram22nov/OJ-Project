from django.urls import path
from compiler import views

urlpatterns = [
    path("", views.submit, name="submit"),
]