from django.contrib import admin
from app.models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'apePaterno', 'apeMaterno', 'numero_servidor', 'area', 'extension')
    raw_id_fields = ('usuario',)
    list_filter = ('area',)
    search_fields = ('usuario__username',)

class NotificadorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apePaterno', 'apeMaterno', 'statusNotificador')

class ServicioAdmin(admin.ModelAdmin):
	list_display = ('id', 'solicitante', 'notificador', 'fechaInicio', 'fechaEnterado', 'fechaFin', 'actividad')
	raw_id_fields = ('solicitante',)
	list_filter = ('notificador', 'actividad', 'solicitante')
	search_fields = ('notificador__nombre', 'solicitante__username', 'sitio__nombre')

class StatusAdmin(admin.ModelAdmin):
	list_display = ("id", "status")

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Notificador, NotificadorAdmin)
admin.site.register(Lugar)
admin.site.register(TipoServicio)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Area)