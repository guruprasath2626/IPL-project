from django.db import models

# Create your models here.
class Teams(models.Model):
    team_name = models.CharField(max_length=500)
    

class Players(models.Model):
    player_name =models.CharField(max_length=500)
    player_number=models.IntegerField()


class PlayerDetails(models.Model):
    player_name=models.ForeignKey('Players', models.DO_NOTHING, blank=True, null=True)
    player_age= models.IntegerField()
    player_position = models.CharField(max_length=500)
    player_team= models.ForeignKey('Teams', models.DO_NOTHING, blank=True, null=True)
    player_rating = models.IntegerField()


class TablePoints(models.Model):
    team_name=models.ForeignKey('Teams',blank=True, null=True)
    win= models.BooleanField()
    lose = models.BooleanField()
    draw = models.IntegerField()
    total_points = models.IntegerField()