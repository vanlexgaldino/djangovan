# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,nome):
    return HttpResponse('<h1>Bem vindo a este ambiente: {}</h1>'.format(nome))