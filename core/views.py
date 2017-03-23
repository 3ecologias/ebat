# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views import generic
from .forms import Call_me

# Create your views here.
class Index(generic.FormView):
	template_name = 'core/index.html'
	form_class = Call_me
	success_url = '/'
	def form_valid(self, form):
		form.send_email()
		messages.success(self.request, 'Tudo certo! Em instantes iremos ligar pra você, não se preocupe!')
		return super(Index, self).form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, 'Algo de errado aconteceu, tente utilizar o nosso serviço de chat.')
		return super(Inxed, self).form_invalid(form)
