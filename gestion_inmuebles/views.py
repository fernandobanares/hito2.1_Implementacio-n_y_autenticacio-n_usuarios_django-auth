from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
# Vista de inicio de sesión
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Define el template que se usará para el login
    redirect_authenticated_user = False  # Redirige automáticamente si el usuario ya está autenticado


@login_required
def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")
    
@login_required
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/register.html", {"form": form})

# Vista para inicio de sesión
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirige a la página de inicio (cambia a la URL de tu elección)
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

