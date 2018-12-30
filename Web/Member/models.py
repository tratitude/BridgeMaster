from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class table(models.Model):
    time = models.DateTimeField(verbose_name="time",auto_now=True)
    NS_TotalPoint = models.DecimalField(max_digits = 5,decimal_places=0)
    EW_TotalPoint = models.DecimalField(max_digits = 5,decimal_places=0)
    RoundNum = models.DecimalField(max_digits = 2,decimal_places=0)     #總共進行幾個ROUND Eg. 1/4/16
    MachineID = models.DecimalField(max_digits = 2,decimal_places=0)
    def __str__(self):
        return str(self.pk)      #回傳TableID
class tableAdmin(admin.ModelAdmin):
    list_display = ['pk', 'MachineID', 'NS_TotalPoint', 'EW_TotalPoint','RoundNum','time']
    search_fields = ['pk', 'MachineID', 'NS_TotalPoint', 'EW_TotalPoint','RoundNum','time']
    ordering = ['pk']


class seat(models.Model):
    class Meta:
        unique_together = (('position','TableID'),('PlayerID','TableID'))
    position = models.CharField(max_length=1)   #Eg. N/E/W/S
    TableID = models.ForeignKey('table',on_delete=models.CASCADE)
    PlayerID = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.TableID)     #回傳TableID
class seatAdmin(admin.ModelAdmin):
    list_display = ['PlayerID','TableID','position']
    search_fields = ['PlayerID','TableID','position']
    ordering = ['PlayerID']


#一場完整的牌局資訊
class rounds(models.Model):
   # dealer=models.CharField(max_length=2)  ??我不知道這要幹嘛
    T_id = models.ForeignKey('table', on_delete=models.CASCADE)
    bid = models.CharField(max_length = 100)    # 開喊位置+喊牌紀錄 Eg.(3,1NT,PS,3C,3S,4NT)
    leader = models.DecimalField(max_digits = 1,decimal_places=0)      # 首引位置
    contract = models.CharField(max_length = 2)      #該局的王牌花色
   # 各家手牌 OrderBy出牌順序 Eg.(SA,SK,SQ,SJ,HA,HK,HQ,HJ.....)
    N = models.CharField(max_length = 38)
    E = models.CharField(max_length = 38)
    W = models.CharField(max_length = 38)
    S = models.CharField(max_length = 38)
   #身價
    NS = models.BooleanField()
    EW = models.BooleanField()
   #吃下的噔數
    NS_Trick = models.DecimalField(max_digits =1,decimal_places=0)
    EW_Trick = models.DecimalField(max_digits=1,decimal_places=0)
    def __str__(self):
        return str(self.T_id)        #回傳TableID
class roundsAdmin(admin.ModelAdmin):
    list_display = ['T_id','NS','EW','NS_Trick','EW_Trick']
    search_fields = ['T_id','NS','EW','NS_Trick','EW_Trick']
    ordering = ['T_id']


admin.site.register(table,tableAdmin)
admin.site.register(seat,seatAdmin)
admin.site.register(rounds,roundsAdmin)