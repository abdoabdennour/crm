from django.urls import path
from . import views


app_name = 'commande' 
urlpatterns = [
path ('ajouter', views.ajouter_commande, name = 'ajouter'),
path ('suprimer/<str:pk>', views.sprimer_commande, name = 'suprimer'),
path ('<str:pk>', views.modifier_commande, name = 'modifier'),
]