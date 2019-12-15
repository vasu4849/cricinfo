from django.db import models
#from cricinfo.teams.models import Team
from teams.models import Team
from django.urls import reverse


# Create your models here.
class Player(models.Model):
    BATSMAN = 'BAT'
    BOWLER = 'BOW'
    KEEPER = 'WCK'
    ALLROUNDER = 'ALL'

    PLAYER_SKILLS = (
        (BATSMAN, 'BATSMAN'),
        (BOWLER, 'BLOWLER'),
        (KEEPER, 'WICKETKEEPER'),
        (ALLROUNDER, 'ALLROUNDER')
    )

    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    profile = models.ImageField(upload_to='media/player', max_length=100)
    skill = models.CharField(max_length=100, choices=PLAYER_SKILLS, default='Batsmen')
    jerseyno = models.IntegerField()
    state = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + " " + self.lastname

    def get_absolute_url(self):
        return reverse('player:player_detail', kwargs={'pk':self.pk})

#Team.objects.filter(player__team__name='Team India')
#Player.objects.filter(team=15) get team india players