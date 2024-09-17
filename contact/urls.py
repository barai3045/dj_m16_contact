from django.urls import path, include
from .import views

urlpatterns = [
     path('', views.home, name='home'),
    path('add/', views.add_contact, name='add_contact'),
    path('view/<int:pk>/', views.view_contact, name='view_contact'),
    path('update/<int:pk>/', views.update_contact, name='update_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    
]