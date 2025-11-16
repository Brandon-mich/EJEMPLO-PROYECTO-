from django.shortcuts import render

def home(request): 
    return render(request, "impresion_de_rectas_numericas/home.html") 

