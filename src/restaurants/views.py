from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import random
# Create your views here.
# function based view


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        randint = random.randint(0, 1000000)
        context = {"randint": randint}
        return context
