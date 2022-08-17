from django.urls import path
from . import views


app_name = 'produit' 
urlpatterns = [
path ('', views.produit, name = 'produit'),

]