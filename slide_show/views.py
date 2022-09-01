from django.shortcuts import render
from django.http import HttpResponse
import json

from slide_show.models import SlideShow


def index(request):
    slides = SlideShow.objects.all()
    return HttpResponse(slides)
