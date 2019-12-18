from django.shortcuts import render
from .models import Player
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class PlayerList(ListView):
    model = Player


class PlayerDetail(DetailView):
    model = Player


class PlayerCreate(CreateView):
    model = Player
    fields = ('firstname', 'lastname', 'profile', 'skill', 'jerseyno', 'state', 'team')


class PlayerUpdate(UpdateView):
    model = Player



class PlayerDelete(DeleteView):
    model = Player
