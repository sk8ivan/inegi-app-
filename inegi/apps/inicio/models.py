from django.db import models

class SistemaOperativo(models.Model):
	idSo = models.AutoField(primary_key = True)
	nombreSistema = models.CharField(max_length = 20)

	def __str__(self):
		return self.nombreSistema


class Equipo(models.Model):
	idEquipo = models.AutoField(primary_key = True)
	nombreEquipo = models.CharField(max_length = 15)

	def __str__(self):
		return self.nombreEquipo

class Parche(models.Model):
	
	IdParche= models.AutoField(primary_key = True)
	nombreParche= models.CharField(max_length = 50)
	ParcheFecha = models.DateTimeField()
	fechaAviso = models.DateTimeField()
	descripcion = models.TextField()
	fechaInstalacion = models.DateTimeField()
	sistema = models.ForeignKey(SistemaOperativo)
	

	def __str__(self):
		return self.nombreParche

class File(models.Model):
	clavefile = models.AutoField(primary_key = True)
	docfile = models.FileField(upload_to='Windows')
	
	def __int__(self):
		return self.clavefile

class Update(models.Model):
	claveUpdate = models.AutoField(primary_key = True)
	docUpdate = models.FileField(upload_to='Update')  
	idEquipo = models.ForeignKey(Equipo)

	def __str__(self):
		return self.idEquipo