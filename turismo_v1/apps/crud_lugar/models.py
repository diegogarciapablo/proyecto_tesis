from django.db import models
from datetime import datetime 
from time import time

tipo_choices=(
	('colegio','Colegio'),
	('iglesia','Iglesia'),
	('plaza','Plaza'),
	('restaurante','Restaurante'),
	('alojamiento','Alojamiento'),
	)

class admin_agregar (models.Model):
	cod_ubicacion= models.AutoField(primary_key = True)
	latitud = models.CharField(max_length=200, blank=False, null=False)
	longitud = models.CharField(max_length=200, blank=False, null=False)
	tipo = models.CharField(max_length=200, blank=False, null=False, choices=tipo_choices)
	def __str__(self):
		return self.tipo+' '+str(self.cod_ubicacion)

class colegio(models.Model):
	cod_colegio=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=200, blank=False, null=False)
	fecha_fundacion = models.DateField(editable=True)
	clasificacion = models.CharField(max_length=200, blank=False)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)

class iglesia(models.Model):
	cod_iglesia=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=200, blank=False, null=False)
	fecha_fundacion = models.DateField(editable=True)
	religion= models.CharField(max_length=200, blank=False, null=False)
	capacidad=models.CharField(max_length=200, blank=False, null=False)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)

class alojamiento(models.Model):
	cod_alojamiento=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=200, blank=False, null=False)
	clasificacion = models.CharField(max_length=200,blank=False, null=False)
	fecha_fundacion = models.DateField(editable=True)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)

class plaza(models.Model):
	cod_plaza=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=200, blank=False, null=False)
	fecha_fundacion = models.DateField(editable=True)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)
	

class restaurante(models.Model):
	cod_restaurante=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=200, blank=False, null=False)
	capacidad=models.CharField(max_length=200, blank=False, null=False)
	clasificacion = models.CharField(max_length=200,blank=False, null=False)
	cod_ubicacion= models.ForeignKey(admin_agregar, on_delete=models.CASCADE)


class evento(models.Model):
	cod_evento=models.AutoField(primary_key=True)
	titulo_evento=models.CharField(max_length=300, blank=False, null=False)
	fecha=models.DateField(editable=True)
	hora_ini=models.TimeField(null=True)
	hora_fin=models.TimeField(null=True)
	descripcion=models.TextField(null=True, max_length=800)

class foto(models.Model):
	cod_foto=models.AutoField(primary_key=True)
	ruta=models.FileField(upload_to='myfolder/', blank=False, null=True)
	cod_evento=models.ForeignKey(evento, on_delete=models.CASCADE)






