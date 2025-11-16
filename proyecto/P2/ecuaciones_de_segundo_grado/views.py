from django.shortcuts import render

def home(request):
    return render(request, "ecuaciones_de_segundo_grado/home.html") 
