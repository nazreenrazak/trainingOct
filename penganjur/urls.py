from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'Penganjur Home'),
	path('aktiviti/add/', views.penganjur_new, name = 'add_aktiviti'),

	]