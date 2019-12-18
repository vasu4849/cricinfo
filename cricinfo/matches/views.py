from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Match


# Create your views here.
class MatchList(ListView):
    model = Match


class MatchDetail(DetailView):
    model = Match


class MatchCreate(CreateView):
    model = Match
    fields = ('first_team', 'second_team', 'status')


class MatchUpdate(UpdateView):
    model = Match
    fields = ['status', 'result']
    template_name_suffix = '_update_form'


class MatchDelete(DeleteView):
    model = Match
    success_url = reverse_lazy('match:match_list')



