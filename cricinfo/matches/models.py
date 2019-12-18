from django.db import models
from django.db.models import Q
from teams.models import Team
from django.urls import reverse


class MatchQuerySet(models.QuerySet):

    def completed_matches(self,):
        return self.filter(status='C')

    def abandoned_matches(self):
        return self.filter(result='NA', status='A')

    def match_fixtures(self):
        return self.filter(result='NA', status='P')

    def ongoing_matches(self):
        return self.filter(status='R')


# Create your models here.
class Match(models.Model):
    DRAW = 'D'
    ABANDONED = 'A'
    COMPLETED = 'C'
    WIN = 'W'
    LOSS = 'L'
    PENDING = 'P'
    RUNNING = 'R'
    GAME_STATUS = (
        (PENDING, 'NOT STARTED'),
        (RUNNING, 'ON GOING'),
        (COMPLETED, 'FINISHED'),
        (ABANDONED, 'ABANDONED'),
    )
    first_team = models.ForeignKey(Team, related_name='match_first_team', on_delete=models.CASCADE, default='')
    second_team = models.ForeignKey(Team, related_name='match_second_team', on_delete=models.CASCADE, default='')
    start_time = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=GAME_STATUS, default=PENDING)
    result = models.CharField(max_length=20, default='NA')

    objects = MatchQuerySet.as_manager()

    def __str__(self):
        return self.first_team.name + ' vs ' + self.second_team.name

    def get_absolute_url(self):
        return reverse('match:match_detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name_plural = 'Matches'


