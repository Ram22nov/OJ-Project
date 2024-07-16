from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    
    path("", views.index, name='home'),
    path("practice",views.practice,name='practice'),
    path("discuss",views.discuss,name='discuss'),
    path("contest",views.practice,name='contest'),
    path("profile",views.practice,name='profile'),
]