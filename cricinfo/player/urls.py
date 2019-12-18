from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path('', views.PlayerList.as_view(), name='player_list'),
    path('players/<int:pk>', views.PlayerDetail.as_view(), name='player_detail'),
    path('create', views.PlayerCreate.as_view(), name='player_create'),
    #path('update/<int:pk>', views.PlayerUpdate.as_view(), name='player_update'),
    #path('delete/<int:pk>', views.PlayerDelete.as_view(), name='player_delete'),
]