from django.urls import path
from . import views



app_name = 'player'

urlpatterns = [
    path('', views.PlayerList.as_view(), name='player_list'),
    path('player/<int:pk>', views.PlayerDetail.as_view(), name='player_detail'),
    path('create', views.PlayerCreate.as_view(), name='player_create'),
    #path('update/<int:pk>', views.TeamUpdate.as_view(), name='team_update'),
    #path('delete/<int:pk>', views.TeamDelete.as_view(), name='team_delete'),
]