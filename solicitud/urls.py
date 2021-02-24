from django.urls import path
from . import views

urlpatterns = [
	path('setsolicitud',views.guardarSolicitud,name='index'),
	path('index', views.index),
	path('listarasignaciones', views.listarAsingnaciones, name="asignaciones"),
	path('solicitudes/', views.listaSolicitudes,  name='solicitud'),
	path('pdf',views.some_view, name='hello.pdf'),
]