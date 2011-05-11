# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from main.models import Image

def index(request):
    image = Image.objects.get(pk=1)
    return render_to_response('index.html', {'image': image})
