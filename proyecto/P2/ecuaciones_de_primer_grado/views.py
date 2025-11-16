from django.shortcuts import render

def home(request): 
    return render(request, "ecuaciones_de_primer_grado/home.html") 
    
