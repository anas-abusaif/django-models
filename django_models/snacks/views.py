from django.shortcuts import render
from django.views.generic import ListView
from snacks.models import Snack
from django.views.generic import DetailView

# Create your views here.

class SnackListView(ListView):
  template_name='snacks_list.html'
  model = Snack

class SnackDetailView(DetailView):
  template_name='snack_detail.html'
  context_object_name = 'snack_object'
  model = Snack
