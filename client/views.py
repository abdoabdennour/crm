from django.shortcuts import redirect,render
from django.urls import reverse
from .models import Client
from.form import Client_form
from commande.models import Commande
from produit.decorators import loginrequis


def client (request,pk):
    clients = Client.objects.get(id=pk)
    commande=clients.commande_clinet.all
    #total_commande = clients.commande_clinet.all.count()
    context = {'clinet':clients,'commande':commande }

    return render (request , 'dètalle_clients.html',context ) 

@loginrequis
def ajouter_client (request):
    if request.method=='POST':
        form = Client_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('produit:produit'))    

    else:
        form = Client_form()
    return render(request,'ajouter_client.html',{'form':form} ) 
   
def modifier_client(request,pk):
    client = Client.objects.get(id =pk)
    if request.method=='POST':
        form = Client_form(request.POST,instance = client)
        if form.is_valid():
            form.save()
        return redirect(reverse('produit:produit'))    

    else:
        form = Client_form(instance = client)
    return render(request,'modifier_client.html',{'form':form})    