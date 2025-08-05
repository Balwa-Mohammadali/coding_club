from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('apply/', views.apply_view, name='apply'),
    
]