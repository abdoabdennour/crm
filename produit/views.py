from django.shortcuts import redirect,render
from django.urls import reverse
from client.models import Client
from commande.models import Commande


def produit (request):
    clients = Client.objects.all()
    commands = Commande.objects.all()
    nombre_client = clients.count()
    nombre_commande = commands.count()
    context = {'clients':clients,'commands':commands ,'nombre_client':nombre_client,'nombre_commande':nombre_commande}
    nombre_client = clients.count()

    return render (request , 'liste_produits.html',context ) 

