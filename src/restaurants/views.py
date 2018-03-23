from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
# function based view



def home(request):
    randint = random.randint(0, 1000000)
    context = {"randint": randint}
    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def contact(request):
    context ={}
    return render(request, "contact.html", context)
