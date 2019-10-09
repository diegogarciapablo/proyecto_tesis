from django.db import models

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


class colegio(models.Model):
	cod_colegio=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=200, blank=False, null=False)
	fecha_fundacion = models.CharField(max_length=200,blank=False, null=False)
	clasificacion = models.CharField(max_length=200, blank=False)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)
