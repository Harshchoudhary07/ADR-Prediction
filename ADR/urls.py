from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adr-checker/', views.adr_checker, name='adr_checker'),
]
