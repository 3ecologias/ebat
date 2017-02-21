from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views import generic

# Create your views here.
def fullsite(request):
	context_general = {}
	return render(request, 'core/index.html', context_general)
