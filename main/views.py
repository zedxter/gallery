# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from main.models import Image

def index(request):
    images = Image.objects.all()
    return render_to_response('index.html', {'images': images})
