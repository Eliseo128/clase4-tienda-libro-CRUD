from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} by {self.autor} - ${self.precio:.2f}"