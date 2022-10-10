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
    data = json.loads(request.body)
    slide = SlideShow(
        title=data['title'],
        description=data['description'],
        user_id=data['user'],
        secret_number=secret_number
    )
    return HttpResponse(slide.secret_number)