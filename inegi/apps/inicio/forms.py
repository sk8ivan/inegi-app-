from django import forms
from django.forms import ModelForm
from .models import Parche, File, Equipo

#FORMULARIO UPDATE

class Windows(ModelForm):
	
	class Meta:
		model = File


class Parches(ModelForm):
	
	class Meta:
		model = Parche

class Prueba(ModelForm):
	
	class Meta:
		model = Equipo