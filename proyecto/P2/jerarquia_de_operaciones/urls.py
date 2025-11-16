from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.home, name="jerarquia_de_operaciones_home")
] 