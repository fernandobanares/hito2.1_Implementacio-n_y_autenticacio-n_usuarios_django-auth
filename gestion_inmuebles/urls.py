from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # URL para el registro
    path('login/', views.CustomLoginView.as_view(), name='login'),  # URL para iniciar sesión
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
]
