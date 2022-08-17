from django.db import models
from client.models import Client
from produit.models import Produit

# Create your models here.
etat = (
    ('en instant','en instant'),
    ('livrè','livrè'),
    ('non livrè','non livrè'),
)

class Commande (models.Model):
    client = models.ForeignKey(Client,related_name='commande_clinet', on_delete = models.CASCADE )
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE )
    date_crèation = models.DateTimeField(auto_now=True)
    etat = models.CharField(max_length=50,choices=etat )


    def __str__(self):
        return self.produit.nom