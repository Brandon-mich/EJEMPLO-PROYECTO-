from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="calculo_de_areas_figuras_planas_home")
] 