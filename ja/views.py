from django.shortcuts import render
from ja.forms import JAForm
from multipageform.views import MultipageFormView
from django.views.generic import TemplateView
# Create your views here.

class JAView(MultipageFormView):
    template_name = 'ja/form_page.html'
    form_class = JAForm
    success_url = 'ja:thank_you'


class JAThankYouView(TemplateView):
    template_name = 'ja/thank_you.html'
