from django.urls import path

from core.views import *

urlpatterns = [
    path('', Home2.as_view()),
]