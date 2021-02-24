from django.contrib import admin
from . models import Empleado, EstadoEmpleado, Cargo, Zona, Area, Punto 


# Register your models here.

admin.site.register(EstadoEmpleado)
admin.site.register(Cargo)
admin.site.register(Zona)
admin.site.register(Area)
admin.site.register(Punto)

class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('ci','nombre','cargo','estado','telefono','costo')

admin.site.register(Empleado, EmpleadoAdmin)
