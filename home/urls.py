from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    
    path("", views.index, name='home'),
    #path("practice",views.practice,name='practice'),
    path("discuss",views.discuss,name='discuss'),
    path("contest",views.contest,name='contest'),
    path("profile",views.profile,name='profile'),
    path('practice/', views.problem_list, name='problem_list'),
    path('practice/<int:problem_id>/', views.problem_detail, name='problem_detail'),
]