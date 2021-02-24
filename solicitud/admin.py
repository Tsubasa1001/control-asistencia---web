from django.contrib import admin
from . models import EstadoSolicitud, TipoSolicitud, Asignacion, Solicitud 
# Register your models here.

admin.site.register(EstadoSolicitud)
admin.site.register(TipoSolicitud)


class AsignacionAdmin(admin.ModelAdmin):
	list_display = ('hora_inicio','hora_fin','empleado','solicitud', 'material')

admin.site.register(Asignacion, AsignacionAdmin)

class SolitudAdmin(admin.ModelAdmin):
	list_display = ('tipo','cliente','estado','hora')

admin.site.register(Solicitud, SolitudAdmin)