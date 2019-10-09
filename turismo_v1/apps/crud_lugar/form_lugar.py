from django import forms
from .models import admin_agregar


class formlugar(forms.ModelForm):
	class Meta:
		model= admin_agregar
		fields = ['latitud','longitud','tipo']
