from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def denetim(request):
    return HttpResponse("Denetim bölümü")

