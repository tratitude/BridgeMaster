from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class table(models.Model):
    time=models.DateTimeField(verbose_name="time",auto_now=True)
    NS
    EW
    
class seat(models.Model):
    position=models.CharField(max_length=1)
    table_ID=models.ForeignKey('table',on_delete=models.CASCADE)
    player_ID=models.ForeignKey('user',on_delete=models.DO_NOTHING)

class rounds(models.Model):
    dealer=models.CharField(max_length=2)
    bid
    leadplayer
    N
    E
    W
    S
    vunerable
    NS
    EW
    game_type
    table_ID==models.ForeignKey('table',on_delete=models.CASCADE)

class player_cards(models.Model):
    card=models.CharField(max_length=2)
    round_ID=models.ForeignKey('rounds',on_delete=models.CASCADE)
    seat_ID=models.ForeignKey('seat',on_delete=models.CASCADE)
    
