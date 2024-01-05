"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from charo.views import home,detail,search,voiture_dispo,contact,CommandeCreateView,recup

urlpatterns = [ # qui veut dit que si l'utilsateur entre admin apres la racine ça l'envoi sur la page administrateur
    path('admin/', admin.site.urls),
    path("",home,name="home"), # si la apres la racine c'est blog alors il va incluire toute les urls qui sont urls.py  depuis blog
    path("article/<int:id_article>",detail,name="detail"), # on a creer un url qui permet d'avoir plus de detail sur un article
    path("article/recherche",search,name="search"),# tu vas dans article tu va cliquer sur recherche et on va appeler la fonctions search depuis views
 #   path("message-sms",sms,name="sms"),
    path("voitures/",voiture_dispo,name="voiture_dispo"),
    path('commande/<int:id_article>', CommandeCreateView.as_view(), name='commande'),
    path('afficher/<int:id_commande>/', recup, name='afficher'),
    path("contact/",contact,name="contact"),   
    path("auth/",include("app_auth.urls")),
    path("my-admin/",include("app_admin.urls")),
 #   path('reserver',reserver_article.as_view(),name='reserver')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # obligatoire 
