# on va lier l'application à blog donc pour le faire : 
# il nous faut la fonction path 

from django.urls import path
from . import views # le point veut dire dans le dossier dans laquelle nous sommes

urlpatterns=[

    path("",views.home,name="home") # tu appele la fonction home de view.home des que le server est lancé et apres charo
# il prend trois paramettre le chemin ,la fonction et le nom qu'on donne à notre chemin url

]