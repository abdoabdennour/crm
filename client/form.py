from django import forms
from .models import Client



class Client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__' 
