from django.shortcuts import render

def home(request): 
    return render(request, "jerarquia_de_operaciones/home.html") 
