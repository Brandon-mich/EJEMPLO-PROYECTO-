from django.shortcuts import render

def home(request):
    return render(request, "operaciones_con_polinomios/home.html") 
