from django.urls import path
from . import views

urlpatterns = [
	#path('',views.index,name='index'),
	path('clientes/', views.listaCliente,  name='cliente'),
	path('login', views.login, name='login')
]