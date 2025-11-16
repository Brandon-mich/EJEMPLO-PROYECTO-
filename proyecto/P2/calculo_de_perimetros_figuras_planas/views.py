from django.shortcuts import render

def home(request):
    return render(request, "calculo_de_perimetros_figuras_planas/home.html") 