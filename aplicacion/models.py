from django.db import models

# Create your models here.
class Cliente(models.Model):
	Nombre = models.CharField(max_length=35)
	Apellido = models.CharField(max_length=35)
	Direccion = models.CharField(max_length=35)
	Ciudad = models.CharField(max_length=35)
	Comuna = models.CharField(max_length=20)
	Telefono = models.IntegerField()
	Correo = models.EmailField(max_length=35)

	def NombreCompleto(self):
		cadena = "{0} {1}"
		return cadena.format(self.Apellido , self.Nombre)
	def __str__(self):
		return self.NombreCompleto()

class Ascensor(models.Model):
	id_ascensor = models.IntegerField()
	Modelo = models.CharField(max_length=20)
	Fallas = models.CharField(max_length=60)
	Reparaciones = models.CharField(max_length=60)
	Piezasremplazadas = models.CharField(max_length=60)

	def __str__(self):
		cadena = "{0} {1} {2} {3} {4}"
		return cadena.format(self.id_ascensor , self.Modelo, self.Fallas , self.Reparaciones,self.Piezasremplazadas)
		def __str__(self):
			return self.DatosAscensor()


class OrdenTrabajo(models.Model):
	Cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
	Ascensor = models.ForeignKey(Ascensor, null=False, blank=False, on_delete=models.CASCADE)
	Folio = models.IntegerField()
	Fecha = models.DateTimeField(auto_now_add=True)
	Fechatermino = models.DateTimeField()
	def __str__(self):
		cadena = "{0} => {1}"
		return cadena.format(self.Cliente, self.Ascensor)



