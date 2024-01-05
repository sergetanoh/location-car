from django.urls import path
from .views import *

urlpatterns=[
     path('',dashboard,name='dashboard'),
    path('my-article',user_article,name='my-article'),
    path('ajouter-article',Add_article.as_view(),name='ajout-article'),
    path('modifier-article/<int:pk>',update_article.as_view(),name='modif'),
    path('suprimer-article/<int:pk>',delete_article.as_view(),name='suprimer'),
    path('suprimer-commande/<int:pk>',delete_commande.as_view(),name='delete'),
    path('search',search,name='search1'),



]