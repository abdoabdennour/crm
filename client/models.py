from django.db import models

# Create your models here.

class Client (models.Model):
    nom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    date_crèation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom