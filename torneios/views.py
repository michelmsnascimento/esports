from django.shortcuts import render


# Create your views here.

def torneios(request):
   return render(request, 'torneios/torneios.html')
