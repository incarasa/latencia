from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.nombre)
    
class Pago(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    valor = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)