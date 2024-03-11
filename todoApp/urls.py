
from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'), 
    path('dashboard/', views.create_get, name='create_get'), 
    path('update/<str:pk>/', views.update_todo, name='update_todo'),
    path('delete/<str:pk>/', views.delete_todo, name='delete_todo'),
    path('register/', views.signupView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]