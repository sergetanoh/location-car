from django import forms
from .models import Article,Commande

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["nom","Category","description","kilometrage","transmission","carburant","image1","image2","image3","prix"]
        labels={"nom":"nom","Category":"categorie","description":"description","kilometrage":"kilometrage","transmission":"transmission","carburant":"carburant","image1":"image1","image2":"image2","image3":"image3","prix":"prix"}
        widgets={
            "nom":forms.TextInput(attrs={'class':'form-control'}),
            "Category":forms.Select(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control','rows':5}),
            "kilometrage":forms.TextInput(attrs={'class':'form-control'}),
            "transmission":forms.TextInput(attrs={'class':'form-control'}),
            "carburant":forms.TextInput(attrs={'class':'form-control'}),
            "image1":forms.FileInput(attrs={'class':'form-control'}),
            "image2":forms.FileInput(attrs={'class':'form-control'}),
            "image3":forms.FileInput(attrs={'class':'form-control'}),
            "prix":forms.NumberInput(attrs={'class':'form-control'}),
        }

class ReserverForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom', 'prenom', 'email', 'date_debut', 'nbre_jours', 'numero']

    widgets = {
        'nom': forms.TextInput(attrs={'class': 'form-control'}),
        'prenom': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'date_debut': forms.DateInput(attrs={'class': 'form-control'}),
        'nbre_jours': forms.NumberInput(attrs={'class': 'form-control'}),
        'numero': forms.TextInput(attrs={'class': 'form-control'}),
    }
    
        

