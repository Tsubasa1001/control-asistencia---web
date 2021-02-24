from django.shortcuts import render
from .models import Material
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core import serializers
# Create your views here.

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


	from django.core import serializers
@csrf_exempt
def listaMateriales(request):
	list_materiales = serializers.serialize("json",Material.objects.all())
	data = {}
	data["materiales"] = list_materiales
	return JsonResponse(data)




