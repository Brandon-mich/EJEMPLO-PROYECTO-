from django.urls import include, path
from django.contrib import admin 
 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core", include("core.urls")),
    path("suma/", include("suma.urls")),
    path("resta/", include("resta.urls")),
    path("multiplicacion/", include("multiplicacion.urls")),
    path("division/", include("division.urls")),
    path("jerarquia_de_operaciones/", include("jerarquia_de_operaciones.urls")),
    path("operaciones_con_polinomios/", include("operaciones_con_polinomios.urls")),
    path("factorizacion/", include("factorizacion.urls")),
    path("impresion_de_rectas_numericas/", include("impresion_de_rectas_numericas.urls")),
    path("ecuaciones_de_primer_grado/", include("ecuaciones_de_primer_grado.urls")),
    path("ecuaciones_de_segundo_grado/", include("ecuaciones_de_segundo_grado.urls")),
    path("calculo_de_areas_figuras_planas/", include("calculo_de_areas_figuras_planas.urls")),
    path("calculo_de_perimetros_figuras_planas/", include("calculo_de_perimetros_figuras_planas.urls")), 
] 
