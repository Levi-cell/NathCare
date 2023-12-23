from django.urls import path
from . import views

urlpatterns = [
    path('solicitar_consultas/', views.solicitar_consultas, name='solicitar_consultas'),
    path('solicitar_profissionais/', views.solicitar_profissionais, name='solicitar_profissionais')
]
