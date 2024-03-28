from django.db import models

# Create your models here.
class Teams(models.Model):
    team_name = models.CharField(max_length=500)

    def __str__(self):
        return self.team_name        

class Players(models.Model):
    player_name =models.CharField(max_length=500)
    player_number=models.IntegerField()

    def __str__(self):
        return self.player_name 

class PlayerDetails(models.Model):
    player_name=models.ForeignKey('Players', models.DO_NOTHING, blank=True, null=True)
    player_age= models.IntegerField()
    player_position = models.CharField(max_length=500)
    player_team= models.ForeignKey('Teams', models.DO_NOTHING, blank=True, null=True)
    player_rating = models.IntegerField()

    def __str__(self):
        return self.player_position
    

class TablePoints(models.Model):
    team_name=models.ForeignKey('Teams',models.DO_NOTHING,blank=True, null=True)
    win= models.BooleanField()
    lose = models.BooleanField()
    draw = models.IntegerField()
    total_points = models.IntegerField
    
    
    def __str__(self):
        return self.total_points
    