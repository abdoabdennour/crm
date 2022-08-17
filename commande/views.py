from django.shortcuts import redirect, render
from django.urls import reverse
from.form import Ajouter_commande
from .models import Commande

# Create your views here.
def ajouter_commande(request):
    if request.method=='POST':
        form = Ajouter_commande(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('produit:produit'))    

    else:
        form = Ajouter_commande()
    return render(request,'ajouter_commands.html',{'form':form} )          


def modifier_commande(request,pk):
    commande = Commande.objects.get(id =pk)
    if request.method=='POST':
        form = Ajouter_commande(request.POST,instance = commande)
        if form.is_valid():
            form.save()
        return redirect(reverse('produit:produit'))    

    else:
        form = Ajouter_commande(instance = commande)
    return render(request,'modifier_commande.html',{'form':form})       




def sprimer_commande(request,pk):
    commande = Commande.objects.get(id =pk)
    context = {'commande':commande }
    if request.method=='POST':
        commande.delete()
        return redirect(reverse('produit:produit'))      
    return render(request,'suprimer_commande.html',context)     