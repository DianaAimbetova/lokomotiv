from django.shortcuts import render
from .models import Scheme

# Create your views here.
def show_schemes(request):
    return render(request, 'tree/menu.html', {'schemes' : Scheme.objects.all()})
