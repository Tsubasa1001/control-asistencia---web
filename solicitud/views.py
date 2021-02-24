from django.shortcuts import render
from .models import Solicitud, TipoSolicitud, EstadoSolicitud
from django.views.decorators.csrf import csrf_exempt
from cliente.models import Cliente
from .models import Asignacion
from empleado.models import Empleado
from empleado.views import listaEmpleados
from django.http import JsonResponse
import json

###########metodo para que se vea las limpio el codigo que se pasa a json############## 

def index(request):
	return render(request, 'solicitud/index.html')

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
def listaSolicitudes(request):
	list_solicitud = serializers.serialize("json",Solicitud.objects.all())
	data = {}
	data["solicitud"] = list_solicitud
	return JsonResponse(data)
#########################################################################################

@csrf_exempt
def guardarSolicitud(request):
	id = request.POST.get("id")
	print(id)
	horaS = '2018-09-25 17:49' #request.POST.get("hora")
	estadoS = EstadoSolicitud.objects.get(nombre=request.POST.get("estado"))
	detalleS = request.POST.get("detalle")
	tipoS = TipoSolicitud.objects.get(nombre=request.POST.get("tipo"))
	clienteS = Cliente.objects.get(ci=request.POST.get("cliente"))
	solicitud = Solicitud(hora=horaS, detalle=detalleS, cliente=clienteS, tipo= tipoS, estado=estadoS, idm=id)
	solicitud.save()
	data = {}
	data["respuesta"] = "OK"
	return JsonResponse(data)


import json
from django.core import serializers

@csrf_exempt
def listarAsingnaciones(request):
	ci = request.POST.get("ci")
	empleado = Empleado.objects.get(ci=ci)
	lista = list(Asignacion.objects.filter(empleado=empleado.id)) 
	solicitudes = []
	for object in lista:
		solicitudes.append(object.solicitud.idm)
	list_asignaciones = serializers.serialize("json", Asignacion.objects.filter(empleado=empleado.id))
	data = {}
	data["asignacion"] = list_asignaciones
	data["solicitudes"] = solicitudes
	return JsonResponse(data)


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

# Create your views here.

#def asignarEmpleado(request):
#	lista = listaEmpleados
#	For i in lista:
#		if(empleado.objects.get(zona=zona))==cliente.objects.get(zona=zona):
#			if(empleado.objects.get(nroTrabajo=nroTrabajo))<5:
#				return ci;