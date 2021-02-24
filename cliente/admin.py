from django.contrib import admin
from . models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('ci','nombre','nro_contrato','direccion')

admin.site.register(Cliente, ClienteAdmin)