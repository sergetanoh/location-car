from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
# je vais creer ma premiere classe
# une fois finis la migration nous allons dans admin.py
class category(models.Model): # elle va heriter d'une clee etrangere chaque fois on creer une classe il faut fait la migrations vers la base de donnees
    name=models.CharField(max_length=120) 
    
    def __str__(self):
        return self.name# veut dire que si on veut afficher un element il suffit uniquement du nom de la ctegories dans le cote administrateur quand on 
    # on ajoute une categorie  c'et le nom ce la categories on vois

class Article(models.Model):# forcement heriter de la classe models.model qui est un module python
    # nous allons lister les attributs de notre classe qui vont representer les champs de notre table
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    nom=models.CharField(max_length=50,default="non name") # le titre qui sera en chaine de caractere et qui à pour taille 50
    Category=models.ForeignKey(category,on_delete=models.CASCADE) # la clee etrangere  puis cascade pour la supression de toutes les articles d'une categories
    description=models.TextField() # la description aura comme type texte
    kilometrage=models.CharField(max_length=50,default="1")
    transmission=models.CharField(max_length=50,default="1")
    carburant=models.CharField(max_length=100,default="1")
    prix = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    image1=models.ImageField(blank=True) # on declare notre image de type image
    image2=models.ImageField(null=True,blank=True) # on declare notre image de type image
    image3=models.ImageField(null=True,blank=True) # on declare notre image de type image
    
    created_at=models.DateTimeField(auto_now_add=True)# veut dire de mettre la date actuel  lorsqu'on ajoute un element
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom # veut dire que si on veut afficher un element il suffit uniquement du titre dans le cote administrateur quand on 
    # on ajoute un article  c'et le nom ce l'article on vois
    def get_absolute_url(self):
        return reverse("my-article") 

class Commande(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=150)
    email=models.EmailField(max_length=100)
    date_debut=models.DateField(max_length=100)
    nbre_jours=models.PositiveIntegerField()
    numero=models.CharField(max_length=70)
    date_commande = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nom