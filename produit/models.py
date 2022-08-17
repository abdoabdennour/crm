from django.db import models

# Create your models here.
class Tage (models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


Categorie = (
    ('multimudia','multimudia'),
    ('vhècule','vhècule'),
    ('pour maison et jardain','pour maison et jardain'),
    ('habillement','habillement'),
    ('accèsoire','accèsoire'),

)

class Produit (models.Model):
    nom = models.CharField(max_length=50)
    prix = models.IntegerField(default=1)
    date_crèation = models.DateTimeField(auto_now=True)
    Categorie = models.CharField(max_length=50,choices=Categorie )


    def __str__(self):
        return self.nom