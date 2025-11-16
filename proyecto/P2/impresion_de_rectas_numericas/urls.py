from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.home, name="impresion_de_rectas_numericas_home"), 
] 