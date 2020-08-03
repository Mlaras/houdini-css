# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render

# Create your views here.
def index(request):
	return render(request,'index.html')

def index2(request):
	return render(request,'index2.html')