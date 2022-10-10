from random import randint

from django.shortcuts import render
from django.http import HttpResponse
import json

from slide_show.models import SlideShow


def index(request):
    slides = SlideShow.objects.all()
    return HttpResponse(slides)


def create_slide(request):
    secret_number = randint(1, 9999)
    slide = SlideShow(
        title=request.title,
        description=request.description,
        user=request.user,
        secret_number=secret_number
    )
    return HttpResponse(slide.secret_number)