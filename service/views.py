from django.shortcuts import render
from .models import Service
# Create your views here.
def services(request):
    
    context = Service.objects.all()
    
    return render (request, 'service/services.html', {'context':context})
    