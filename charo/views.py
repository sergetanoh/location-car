from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse_lazy
from .models import Article,category,Commande
from django.contrib.auth.models import User
from .forms import ReserverForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
# creation de home
def home(request): # parametre request obligatoire qui va permettre les requettes http
    list_article=Article.objects.all() # tu recupere tout les objets de la classe article pour mettre dans list_article
    context={"liste_articles":list_article}

    return render(request,"index.html",context)# veut dire tu m'envoi un templates appellé index.html
    # je vais dans mon dossier charo pour creer un dossier templates
    # render permet de rendre le fichier html au user et tu vas le rendre avec context
def voiture_dispo(request): 
    list_article=Article.objects.all() # tu recupere tout les objets de la classe article pour mettre dans list_article
    context={"liste_articles":list_article}
    return render(request,"car.html",context)

def contact(request): 
    
    return render(request,"contact.html",)


def detail(request,id_article):
    article=Article.objects.get(id=id_article)# ici on recupere l'id de l'article depuis la database et on met
    # ensemble avec  deails selon l'id recuperer il affichera le detail
    category=article.Category # on va recupere les categories des articles pour mettrez dans la varailbe category
    article_en_relation=Article.objects.filter(Category=category) #puis nous allons flitrer ces valeurs en ciblant les categrories 
    return render(request,"detail.html",{"article":article,"aer":article_en_relation})    # nous allons recupere les articles en relation""""""

def search(request):
    #GET={"article":"cafe"} c'est ce qui ce passe dans la ligne juste apres
    query=request.GET["article"]
    liste_article=Article.objects.filter(nom__icontains=query) # tu vas selectioner tout les objets dont le titre est egale à qruery
    return render(request,"search.html",{"liste_article":liste_article})
    # les ypes de requettes : SELECT *FROM Article where titre LIKE %'query'% veut dit que si il ya des mot dans la demande de l'utilisateur et que notre titre est dedans on envoi la requettes


def sms(request):
    message=request.get["body"]
    message_splet=message.split("-") # permet de distinguer le titre et la description
    titr=message_splet[0]
    description=message_splet[1]

    agri_category=category.objects.get(id=1)
    article=Article(titre=titr,Category=agri_category,description=description,image="http://default")
    article.save()
    print("donnees dauvegardes")
    return HttpResponse("donnees sauvegarder")

""""
def registerreservation_view(request):
    if request.method == 'POST':
        form = reserverForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nom']
            email = form.cleaned_data['prenom']
            password = form.cleaned_data['quartier']
            password = form.cleaned_data['numero']
            User.objects.create(username=username, email=email, password=password)
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login-blog')
    else:
        form = reserverForm()
    return render(request, 'register.html', {'form': form})


"""
class CommandeCreateView(CreateView):
    model = Commande
    form_class = ReserverForm
    template_name = 'comande.html'
    success_url = reverse_lazy("afficher", kwargs={'id_commande': None})

    def get_success_url(self):
        return reverse_lazy("afficher", kwargs={'id_commande': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs['id_article']
        article = Article.objects.get(id=article_id)
        context['article'] = article
        return context
    

    def form_valid(self, form):
        article_id = self.kwargs['id_article']
        article = Article.objects.get(id=article_id)
        form.instance.article = article
        return super(CommandeCreateView, self).form_valid(form)




def recup(request, id_commande):
    commande = Commande.objects.get(id=id_commande)
    article = commande.article
    nom_client = commande.nom
    prenom_client=commande.prenom
    num_client = commande.numero
    date_debut = commande.date_debut
    nbre_jours =commande.nbre_jours

    
    context = {
        "nom_client": nom_client,
        "prenom_client":prenom_client,
        "nom_article": article.nom,
        "numero": num_client,
        "date_debut":date_debut,
        "nbre_jours":nbre_jours,
        "total": ((article.prix * nbre_jours)),
    }

    # Set your Twilio account SID and auth token


    return render(request, "effectuer.html", context)
