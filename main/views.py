# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from main.models import Image, Group

def index(request):
    groups = Group.objects.all()
    return render_to_response('index.html', {'groups': groups})
