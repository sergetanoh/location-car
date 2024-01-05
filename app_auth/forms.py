from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="nom utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))





class RegisterForm(forms.Form):
    username=forms.CharField(label="nom utilisateur",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(label="nom utilisateur",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))
   