from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Match
from .forms import MatchForm


# Create your views here.
class MatchList(ListView):
    model = Match


class MatchDetail(DetailView):
    model = Match


class MatchCreate(CreateView):
    form_class = MatchForm
    model = Match
    #template_name = 'match_form.html'
    #fields = ('first_team', 'second_team', 'result')


class MatchUpdate(UpdateView):
    model = Match
    #fields = ['status', 'result']
    fields = ['first_team', 'second_team', 'result']
    template_name_suffix = '_update_form'


class MatchDelete(DeleteView):
    model = Match
    success_url = reverse_lazy('match:match_list')



