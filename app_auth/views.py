from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                    login(request, user)
                    return redirect('my-article')
                
            else:
                messages.error(request, "Erreur d'authentification.")
        else:
            messages.error(request, "Veuillez remplir tous les champs du formulaire.")
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')




def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login-blog')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


"""


    
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm



"""