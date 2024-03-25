from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

#parte del formulario 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'core/home.html')

#se define interfaz de ti para que redireccione
def creaciondeticket(request):
    return render(request, 'core/creaciondeticket.html')

@login_required
def products(request):
    return render(request, 'core/products.html')

#parte del formulario 
def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Cambia 'home' por la URL de la página a la que deseas redirigir al usuario después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#para devolver error si ingresa mal usuario y contraseña 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationError(data=request.POST)
        if form.is_valid():
            # Lógica para el inicio de sesión exitoso
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


