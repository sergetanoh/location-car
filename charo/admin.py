from django.contrib import admin
from .models import Article,category,Commande

#  tous cexux que nous mettons icic permettent a l'administrateur de travailler
admin.site.register(Article) # dans notre page administrateur il faut mettre aticle labas
admin.site.register(category) # il sera dans notre interface administrateur
admin.site.register(Commande) # il sera dans notre interface administrateur