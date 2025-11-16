from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="operaciones_con_polinomios_home"),
] 