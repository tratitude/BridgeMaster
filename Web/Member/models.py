from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class table(models.Model):
    time = models.DateTimeField(verbose_name="time",auto_now=True)
    NS_TotalPoint = models.DecimalField(max_digits = 5,decimal_places=0)
    EW_TotalPoint = models.DecimalField(max_digits = 5,decimal_places=0)
    RoundNum = models.DecimalField(max_digits = 10,decimal_places=0)     #總共進行幾個ROUND Eg. 1/4/16
    MachineID = models.DecimalField(max_digits = 10,decimal_places=0)
    dds_result = models.CharField(max_length=60, null=True)  # 分析過的存進資料庫
    '''
    dds_result format: string{10 11 12 13 20 ... 53}
    # Use space to seperate each 2 digits numner
        N   E   S   W
    NT 10  11  12  13
    S  20  21  22  23
    H  30  31  32  33
    D  40  41  42  43
    C  50  51  52  53
    '''
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
    PlayerID = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.TableID)     #回傳TableID
class seatAdmin(admin.ModelAdmin):
    list_display = ['PlayerID','TableID','position']
    search_fields = ['PlayerID','TableID','position']
    ordering = ['PlayerID']


#一場完整的牌局資訊
class rounds(models.Model):
   # dealer=models.CharField(max_length=2)  ??我不知道這要幹嘛
    T_id = models.ForeignKey('table', on_delete=models.CASCADE,null=True)
    bid = models.CharField(max_length = 100,null=True)    # 開喊位置+喊牌紀錄 Eg.(3,1NT,PS,3C,3S,4NT)
    leader = models.CharField(max_length = 1)      # 首引位置 N/E/S/W
    contract = models.CharField(max_length = 2)      #該局的王牌花色
# 顯示各家手牌(deal)
    '''
    N   QJ85.AJ64.T85.J4
    E   AK42.75.Q63.9863
    S   T976.8.A942.KT52
    W   3.KQT932.KJ7.AQ7
    '''
    N = models.CharField(max_length = 38)
    E = models.CharField(max_length = 38)
    W = models.CharField(max_length = 38)
    S = models.CharField(max_length = 38)
# 各家手牌 OrderBy出牌順序 Eg.(SA.SK.SQ.SJ.HA.HK.HQ.HJ .....)
    N_play = models.CharField(max_length = 38, null=True)
    E_play = models.CharField(max_length = 38, null=True)
    W_play = models.CharField(max_length = 38, null=True)
    S_play = models.CharField(max_length = 38, null=True)
   #身價
    vulnerable = models.CharField(max_length = 4,null=True)    #None:0, NS:1, EW:2, All:3
   #declarer吃下的噔數
    result = models.DecimalField(max_digits =2,decimal_places=0)
    declarer = models.CharField(max_length =1,null=True)  # N/S/E/W
    Rnum = models.DecimalField(max_digits=2,decimal_places=0,null=True)    #1~16
    score = models.CharField(max_length=100,null=True)   #declarer的得分
    #### Classic Games ###
    Event = models.CharField(max_length=100,null=True)
    Site = models.CharField(max_length=100,null=True)
    Date = models.CharField(max_length=100,null=True)
    dds_result = models.CharField(max_length=60, null=True)  # 分析過的存進資料庫
    '''
    dds_result format: string{10 11 12 13 20 ... 53}
    # Use space to seperate each 2 digits numner
        N   E   S   W
    NT 10  11  12  13
    S  20  21  22  23
    H  30  31  32  33
    D  40  41  42  43
    C  50  51  52  53
    '''

    def __str__(self):
        return str(self.T_id)        #回傳TableID
class roundsAdmin(admin.ModelAdmin):
    list_display = ['pk','T_id','Event','Site','Date','Rnum','declarer','score','result','vulnerable']
    search_fields = ['pk','T_id','Event','Site','Date','Rnum','declarer','score','result','vulnerable']
    ordering = ['T_id']

admin.site.register(table,tableAdmin)
admin.site.register(seat,seatAdmin)
admin.site.register(rounds,roundsAdmin)
