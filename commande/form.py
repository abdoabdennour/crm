from django import forms
from .models import Commande



class Ajouter_commande(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__' 
