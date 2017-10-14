 # howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

class PopupPageView(TemplateView):
    template_name = "popup.html"

class AcceptPageView(TemplateView):
    template_name = "accept.html"

class ThanksPageView(TemplateView):
	template_name = "thanks.html"