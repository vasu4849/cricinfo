from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'teams'

urlpatterns = [
    path('', views.TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),
    path('create', views.TeamCreate.as_view(), name='team_create'),
    path('update/<int:pk>', views.TeamUpdate.as_view(), name='team_update'),
    path('delete/<int:pk>', views.TeamDelete.as_view(), name='team_delete'),
]