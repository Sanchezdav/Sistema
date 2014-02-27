from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
	area = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Areas'

	def __unicode__(self):
		return self.area

class Usuario(models.Model):
	usuario = models.OneToOneField(User)
	apePaterno = models.CharField(max_length=50, verbose_name="Apellido Paterno")
	apeMaterno = models.CharField(max_length=50, verbose_name="Apellido Materno", blank=True, null=True)
	extension = models.IntegerField(blank=True, null=True)
	area = models.ForeignKey(Area, blank=True, null=True)
	numero_servidor = models.CharField(max_length=50, verbose_name="Numero de Servidor", blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Usuarios'

	def __unicode__(self):
		return self.usuario.username

class Status(models.Model):
	status = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Status'

	def __unicode__(self):
		return self.status

class Notificador(models.Model):
	nombre = models.CharField(max_length=50)
	apePaterno = models.CharField(max_length=50, verbose_name="Apelido Paterno", null = True, blank = True)
	apeMaterno = models.CharField(max_length=50, verbose_name="Apelido Materno", null = True, blank = True)
	statusNotificador = models.ForeignKey(Status, verbose_name="Status", default=lambda: Status.objects.get(id=1))

	class Meta:
		verbose_name_plural = 'Notificadores'

	def __unicode__(self):
		return self.nombre

class Lugar(models.Model):
	nombre = models.CharField(max_length=255)
	referencia = models.TextField(null = True, blank = True)

	class Meta:
		verbose_name_plural = 'Lugares'

	def __unicode__(self):
		return self.nombre

class TipoServicio(models.Model):
	tipoServicio = models.CharField(max_length=50, verbose_name="Servicio")

	class Meta:
		verbose_name_plural = 'Tipos de Servicios'

	def __unicode__(self):
		return self.tipoServicio

class Servicio(models.Model):
	solicitante = models.ForeignKey(User)
	notificador = models.ForeignKey(Notificador)
	fechaInicio = models.DateTimeField(auto_now_add=True)
	fechaEnterado = models.DateTimeField(auto_now_add=False, blank=True, null=True)
	fechaFin = models.DateTimeField(auto_now_add=False, blank=True, null=True)
	sitio = models.ForeignKey(Lugar)
	actividad = models.ForeignKey(TipoServicio)
	comentarios = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Servicios'

	def __unicode__(self):
		return unicode(self.id)

report_builder_fieldsets = (
    ('Servicio', {
        'fields': ('solicitante', 'notificador', 'fechaInicio'),
    }),
)