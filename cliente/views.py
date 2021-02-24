from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Cliente
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#def index(request):
#	return render(request, 'blog/index.html')

###########metodo para que se vea las limpio el codigo que se pasa a json############## 
def get_json_list(query_set):
	list_object = []
	for obj in query_set:
		dict_obj = {}
		for field in obj._meta.get_fields():
			try:
				if field.many_to_many:
					dict_obj[field.name] = get_json_list(getattr(obj, field.name).all())
					continue
				dict_obj[field.name] = getattr(obj, field.name)
			except AttributeError:
				continue
		list_object.append(dict_obj)
	return list_object					
#########################################################################################

from django.core import serializers
@csrf_exempt
def listaCliente(request):
	list_clientes = serializers.serialize("json",Cliente.objects.all())
	data = {}
	data["clientes"] = list_clientes
	return JsonResponse(data)


@csrf_exempt
def login(request):
	usernameR = str( request.POST.get("username"))
	passwordR = str(request.POST.get("password"))
	usuario =  Cliente.objects.get(ci=passwordR, nombre=usernameR)
	data = {}
	if(usuario):
		data["result"] = "valido"
	else:
		data["result"] = "invalido"
	return JsonResponse(data)







#def registrarSolicitud(request):
#	solicitud = Solicitud.create("")
