from django.shortcuts import render

def home(request):
    return render(request,'Pagina Principal.html')

