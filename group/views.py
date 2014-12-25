# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext

# Create your views here.

def index(request):
    context = RequestContext(request)
    return render_to_response('Group/index.html', context, {})