from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Team
from player.models import Player


# Create your views here.
class TeamList(ListView):
    model = Team


class TeamDetail(DetailView):
    context_object_name = 'team'
    model = Team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player_list'] = Player.objects.filter(team=self.kwargs['pk'])
        return context


class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'country', 'logo',]


class TeamUpdate(UpdateView):
    model = Team


class TeamDelete(DeleteView):
    model = Team


