from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")
    class Meta:
        managed = False
        db_table = 'public_persona'

class Proveedor(Persona):
    CUIT = models.CharField(max_length=10,verbose_name='CUIT')
    estado = models.BooleanField(default=0)
    class Meta:
        managed = False
        db_table = 'public_proveedor'    

class Interno(Persona):
    CUIL = models.CharField(max_length=10,verbose_name='CUIL')
    estado = models.BooleanField(default=0)
    class Meta:
        managed = False
        db_table = 'public_interno'    
