import datetime

from .models import Profile

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def home(request):
    date = datetime.datetime.now()
    return HttpResponse(date)


class Home2(TemplateView):
    model = Profile
    template_name = 'base/base_template.html'



