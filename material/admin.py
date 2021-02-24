from django.contrib import admin
from . models import Material
# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
	list_display = ('nombre','detalle')

admin.site.register(Material, MaterialAdmin)

	