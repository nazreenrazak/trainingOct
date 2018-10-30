from django.urls import path
from . import views

urlpatterns = [
	#http://127.0.0.1:8000/penganjur/
	path('', views.home, name = 'Penganjur Home'),

	#http://127.0.0.1:8000/penganjur/aktiviti/add/
	path('aktiviti/add/', views.penganjur_new, name = 'add_aktiviti'),

	#http://127.0.0.1:8000/penganjur/aktiviti/<pk>/delete/
	path('aktiviti/<int:pk>/delete/', views.delete_aktiviti, name = 'delete_aktiviti'),
	
	#http://127.0.0.1:8000/penganjur/aktiviti/<pk>/delete/
	path('aktiviti/<int:pk>/edit/', views.edit_aktiviti, name = 'edit_aktiviti'),
	]