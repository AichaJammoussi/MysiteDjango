from django.urls import path,include
from . import views
from .views import CategoryAPIView,ProduitAPIView
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', views.index, name='index'),
path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
path('nouvCommande/', views.nouveaucommende, name='nouvCommande'),
path('nouvProduit/',views.listProduit,name='liste'),

path('register/',views.register, name = 'register'),
 path('api/category/', CategoryAPIView.as_view()),
path('api/produit/',ProduitAPIView.as_view()),

 
  ]