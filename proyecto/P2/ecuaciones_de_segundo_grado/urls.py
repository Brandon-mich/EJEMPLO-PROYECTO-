from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="ecuaciones_de_segundo_grado_home"),
] 