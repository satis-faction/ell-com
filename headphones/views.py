from django.shortcuts import render
from django.http import HttpResponse
from .models import Headphones

def home(request):
    headphones = Headphones.objects.all()
    return render(request, "home.html", {"headphones": headphones})
