from django.urls import path
from . import views


app_name = 'client' 
urlpatterns = [
path ('ajouter', views.ajouter_client, name = 'ajouter'),
path ('modifier/<str:pk>', views.modifier_client, name = 'modifier'),
path ('<str:pk>', views.client, name = 'client'),

]