from django.urls import path
from . import views

app_name = 'match'

urlpatterns = [
    path('', views.MatchList.as_view(), name='match_list'),
    path('match/<int:pk>', views.MatchDetail.as_view(), name='match_detail'),
    path('start', views.MatchCreate.as_view(), name='match_create'),
    path('update/<int:pk>', views.MatchUpdate.as_view(), name='match_update'),
    path('delete/<int:pk>', views.MatchDelete.as_view(), name='match_delete'),
]