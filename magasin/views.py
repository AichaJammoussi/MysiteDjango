from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produit
from django.template import loader
from .models import Fournisseur

from .forms import FournisseurForm
from .forms import ProduitForm
from django.shortcuts import redirect

from .models import Commande
from .forms import CommandeForm
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer, ProduitSerializer

from rest_framework import viewsets

from magasin.models import Produit


def index(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm() 
    
    list = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list})

    #return render(request,'magasin/majProduits.html',{'form':form})


def nouveauFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            form = FournisseurForm()
            return HttpResponseRedirect('/magasin/nouvFournisseur/') 
    else:
        form = FournisseurForm()

    fournisseurs = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'form': form, 'fournisseurs': fournisseurs})
def listProduit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  
    return render(request, 'magasin/majProduits.html', {'form': form})


def nouveaucommende(request) :
    if request.method =='POST' :
        form=CommandeForm(request.POST)
        if form.is_valid() :
            form.save()
    else :
        form=CommandeForm()

    commandes= Commande.objects.all()

    return render(request, 'magasin/Commande.html', {'form': form, 'commandes': commandes})
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(catégorie_id=category_id)
            return queryset