from django.shortcuts import render


# Create your views here.

def esports(request):
   return render(request, 'esports/esports.html')