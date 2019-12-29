from django.db import models
from django.db.models import Q
from teams.models import Team
from django.urls import reverse


class MatchQuerySet(models.QuerySet):

    def completed_matches(self,):
        return self.filter(result='FINISHED')

    def abandoned_matches(self):
        return self.filter(result='ABANDONED')

    def match_fixtures(self):
        return self.filter(result='NOT STARTED')

    def ongoing_matches(self):
        return self.filter(status='ON GOING')


# Create your models here.
class Match(models.Model):
    DRAW = 'D'
    ABANDONED = 'A'
    COMPLETED = 'C'
    WIN = 'W'
    LOSS = 'L'
    PENDING = 'P'
    RUNNING = 'R'
    RESULT = [
        ('NOT STARTED', 'FIXTURE'),
        ('ON GOING', 'IN PROGRESS'),
        ('ABANDONED', 'ABANDONED'),
    ]
    TEAMS = [
        ('--------------------', '---------------------'),
        ('Team Australia', 'Australia Won'),
        ('Team India', 'India Won'),
        ('Team Pakistan', 'Pakistan Won'),
        ('Team South Africa', 'South Africa Won'),
        ('Team Srilanka', 'Srilanka Won'),
        ('Team WestIndies', 'WestIndies Won'),
        ('Team England', 'England Won'),
    ]
    first_team = models.ForeignKey(Team, related_name='match_first_team', on_delete=models.CASCADE, default='')
    second_team = models.ForeignKey(Team, related_name='match_second_team', on_delete=models.CASCADE, default='')
    start_time = models.DateField(auto_now_add=True)
    RESULT.extend(TEAMS)
    result = models.CharField(max_length=100, choices=RESULT, default='')

    objects = MatchQuerySet.as_manager()

    def __str__(self):
        return self.first_team.name + ' vs ' + self.second_team.name

    def get_absolute_url(self):
        return reverse('match:match_detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name_plural = 'Matches'



