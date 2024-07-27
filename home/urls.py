from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    
    path("", views.index, name='home'),
    #path("practice",views.practice,name='practice'),
    
    path("profile/",views.profile,name='profile'),
    path('practice/', views.problem_list, name='problem_list'),
    path('practice/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
]