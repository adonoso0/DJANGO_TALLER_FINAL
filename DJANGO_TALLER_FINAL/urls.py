"""
Definition of urls for DJANGO_TALLER_FINAL.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from serialApp import views

"""""
       path('', views.home, name='home'),
       path('contact/', views.contact, name='contact'),
       path('about/', views.about, name='about'),
       path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
       path('admin/', admin.site.urls),
       """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listaAPI/', views.listaAPI),
    path('inscripciones/', views.listadoInscripciones),
    path('agregarReserva/', views.agregarReserva),
    path('eliminarReserva/<int:id>', views.eliminarReserva),
    path('actualizarReserva/<int:id>', views.actualizarReserva),
    path('institutos/', views.InstitucionLista),
    path('institutos/<int:id>', views.InstitucionDetalle),
    path('jsonInscritos/', views.jsonInscritos),
    path('inscritos/', views.InscritosLista.as_view()),
    path('inscritos/<int:pk>', views.InscritosDetalle.as_view()),
]
