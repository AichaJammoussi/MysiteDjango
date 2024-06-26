from django.db import models
from datetime import date
# Create your models here.

class Categorie(models.Model):
    TYPE_CHOICES=[('Al','Alimentaire'), ('Mb','Meuble'),('Sn','Sanitaire'), ('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')] 
    name=models.CharField(max_length=255,choices=TYPE_CHOICES,default='Al')
    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default='sfax')
    email=models.EmailField(default='aa')
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom+ self.adresse + " "+self.email+" "+self.telephone
    



class Produit(models.Model):
    TYPE_CHOICES = [
        ('fr', 'frais'),
        ('cs', 'conserve'),
        ('em', 'emballe')
    ]
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='em')
    catégorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)  # Correction du nom du champ
    img = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.libelle} - {self.description}"



class ProduitNC(Produit) :
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return self.Duree_garantie    




'''class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produit=models.ManyToManyField(Produit)
    
    def __str__(self):
        return str(self.dateCde)+" "+str(self.totalCde)
    def calcul(self):
        return sum(produit.prix for produit in self.produit.all())'''

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField(Produit)
    def str(self) :
        return str(self.dateCde) +" "+str(self.totalCde) 
    def calculer_total (self):
        return sum(Produit.prix for Produit in self.produits.all())