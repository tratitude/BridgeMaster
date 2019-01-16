from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django .utils import timezone
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.sessions.models import Session
from django.views import View
from Member.models import rounds,table,seat
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse
import time,json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date,timedelta
from django.db.models	 import Q
from distutils.util import strtobool
from django.forms.models import model_to_dict
from django.core.paginator import Paginator

# Create your views here.
# superuser admin/admin123
def isset(v):
	try :
		type (eval(v))
	except :
		return  0
	else :
		return  1
def Name(request):
	name = request.user.first_name
	if name == "":
		name = request.user.username
	return name

def login(request):
	if request.user.is_authenticated:		#確認登入狀態
		return redirect("/Member/index/")
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		sessions = Session.objects.filter(expire_date__gt=timezone.now())
		logged_in = []
		for session in sessions:
			user_id = session.get_decoded().get('_auth_user_id')
			logged_in.append(user_id)
		if (user is not None)and str(user.id) in logged_in:
			message = '重複登錄'
		elif (user is not None):
				auth.login(request,user)
				return redirect("/Member/index/")
		else:
			message = '登入失敗！該帳號可能已遭鎖定，請聯繫管理員'
	return render(request, "Member/login.html", locals())

@login_required(login_url='/Member/login/')
def index(request):
	name = Name(request)
	permission = request.user.is_staff
	message="Welcome To BridgeMaster !!!"
	return render(request, "Member/index.html", locals())


def sign_up(request):
	if request.method == 'POST':
		name=request.POST['username']
		firstname = request.POST['firstname']
		password = request.POST['password']
		password2 = request.POST['password2']
		if password!=password2:
			message="請輸入相同密碼"
			return render(request,"Member/sign_up.html",locals())
		try:	#帳號是否重複使用
			User.objects.get(username=name)
			message="帳號已有人使用"
			return render(request, "Member/sign_up.html", locals())			
		except:
			pass
		user=User.objects.create_user(username=name, password=password,first_name=firstname)
		user.is_active=True
		user.save()
		return redirect('/Member/login/')
	return render(request, "Member/sign_up.html", locals())

def logout(request):
	auth.logout(request)   # logout error
	message="登出成功"
	return redirect('/Member/login/')

@login_required(login_url='/Member/login/')
def modify(request):
	user=request.user
	username=user.username
	#name=user.first_name
	if request.method == 'POST':
		new_name= request.POST['firstname']
		user.first_name = new_name
		if	"current_pass" in request.POST:
			cur_pass= request.POST['current_pass']
			new_pass= request.POST['new_pass']
			check_pass= request.POST['check_pass']
		#if new_pass!="": 	#是否修改密碼
			if not user.check_password(cur_pass):					
				message="當前密碼錯誤"
				return render(request,"Member/modify.html",locals())
			if new_pass==""	or new_pass==cur_pass:
				message = "新密碼不可為空或相同"
				return render(request, "Member/modify.html", locals())
			if new_pass!=check_pass:
				message="第二組密碼不符"
				return render(request,"Member/modify.html",locals())
			user.set_password(new_pass)
			User = authenticate(username=username, password=new_pass)  # 直接重新登入
			auth.login(request, User)
		user.save()
		return redirect("/Member/index/")
	return render(request,"Member/modify.html",locals())
@login_required(login_url='/Member/login/')
def modify2(request):
	if request.user.is_staff==False:
		message = "你不是管理員"
		return render(request,"/Member/index/",locals())
	if request.method=="POST":
		unit = User.objects.get(id = request.POST['userid'])
		unit.first_name = request.POST['UserFirstName']
		unit.email = request.POST['UserEmail']
		unit.is_active = strtobool(request.POST['UserActive'])
		unit.save()
		message = "修改成功"
		return redirect("/Member/Administrator/")
	message = "系統錯誤"
	return render(request,"/Member/index/",locals())

def data_fresh(request):
	Users = []
	SessionStore.clear_expired()
	sessions = Session.objects.all()
	#bmbc = request.session['BMBC']
	#print(bmbc)
	try:
		for session in sessions:
			s = session.get_decoded()
			print(s)
			if 'BMBC' in s and s['BMBC']==request.session['BMBC']:		#取出所有BMBC相同的玩家
				Users.append(s['_auth_user_id'])
	except:
		return render(request, "Member/General.html", locals())
	Usernames = []
	for user in Users:
		un = User.objects.get(id=user).username
		Usernames.append(un)
	if len(Usernames)==4:
		Usernames.append("遊戲開始")
	return JsonResponse(Usernames,safe=False)

@csrf_exempt
def State(request):
	BMBC = request.body.decode('utf-8')
	print(BMBC)
	data = 0
	sessions = Session.objects.all()
	try:
		for session in sessions:
			s = session.get_decoded()
			if  'bmbc' in s and BMBC==s['bmbc']:
				data = s
		if data==0:
			return JsonResponse({'state':None})
		return JsonResponse(data)  # 回傳{'bmbc':bmbc ,'state':state}
	except:
		return JsonResponse({'state':None})

@login_required(login_url='/Member/login/')
def Classic(request):
	if request.method=="POST":
		# 禁止短時間內多次創建同主機下的Table
		SessionStore.clear_expired()
		start = timezone.now()-timedelta(minutes=10)
		end = timezone.now()
		if not table.objects.filter(MachineID=request.session['BMBC'],time__range=[start,end]):
				#設置主機狀態表
				Ses = SessionStore()
				Ses['bmbc'] = request.session['BMBC']		##閒置過久session可能過期
				ROUND = rounds.objects.get(pk=request.POST['Game'])
				Ses['from'] = request.POST['Game']
				Ses['round'] = model_to_dict(ROUND, fields=['N','E','W','S'])
				#print(Ses['round'])
				Ses['state'] = '2'
				Ses.set_expiry(300)

				#創建牌桌及座位
				t= table.objects.create(MachineID=request.session['BMBC'],NS_TotalPoint=0,EW_TotalPoint=0,RoundNum=0)
				t.save()
				Ses['T_id'] = t.pk
				Nplayer = User.objects.get_by_natural_key(request.POST['N'])		#若輸入錯誤，將找不到該用戶
				s = seat.objects.create(position='N',PlayerID=Nplayer,TableID=t)
				s.save()
				Eplayer = User.objects.get_by_natural_key(request.POST['E'])  # 若輸入錯誤，將找不到該用戶
				s = seat.objects.create(position='E', PlayerID=Eplayer, TableID=t)
				s.save()
				Splayer = User.objects.get_by_natural_key(request.POST['S'])  # 若輸入錯誤，將找不到該用戶
				s = seat.objects.create(position='S', PlayerID=Splayer, TableID=t)
				s.save()
				Wplayer = User.objects.get_by_natural_key(request.POST['W'])  # 若輸入錯誤，將找不到該用戶
				s = seat.objects.create(position='W', PlayerID=Wplayer, TableID=t)
				s.save()
				Ses.create()
				return redirect("/Member/index/")
		Err = "禁止短時間內多次開局"
		return render(request,"Member/index.html/",locals())
	message = "錯誤方式訪問該頁面"
	return redirect("/Member/login/")

@login_required(login_url='/Member/login/')
def playmode(request,pm='x'):
	name = Name(request)
	if pm!='x':
		if(pm==0):	#Classic
			ClassicGames = rounds.objects.filter(T_id=None,Rnum=0)
			if request.method == "POST" and request.POST['event']:
				ClassicGames = ClassicGames.filter(Event__contains = request.POST['event'])
			return render(request,"Member/Classic.html",locals())
		elif (pm==1):	#General
			Users = []
			SessionStore.clear_expired()
			sessions = Session.objects.all()
			try:
				for session in sessions:
					s = session.get_decoded()
					if 'BMBC' in s and s['BMBC']==request.session['BMBC']:		#取出所有BMBC相同的玩家
						Users.append(s['_auth_user_id'])
			except:
				return render(request, "Member/General.html", locals())
			Usernames = []
			for user in Users:
				username = User.objects.filter(id=user)
				for us in username:
					Usernames.append(us)
			if len(Usernames)>4:
				message = "該房間已客滿!!!"
				return render(request,"Member/index,html",locals())
			elif len(Usernames)==4:
				# 禁止短時間內多次創建同主機下的Table
				if	not table.objects.filter(MachineID=request.session['BMBC'],time__range=[timezone.now()-timedelta(minutes=10),timezone.now()]):
					t = table.objects.create(MachineID=request.session['BMBC'],NS_TotalPoint=0,EW_TotalPoint=0,RoundNum=0)
					t.save()
					N = User.objects.get_by_natural_key(Usernames[0])
					s = seat.objects.create(position='N',PlayerID=N,TableID=t)
					s.save()
					E = User.objects.get_by_natural_key(Usernames[1])
					s = seat.objects.create(position='E', PlayerID=E, TableID=t)
					s.save()
					S = User.objects.get_by_natural_key(Usernames[2])
					s = seat.objects.create(position='W', PlayerID=S, TableID=t)
					s.save()
					W = User.objects.get_by_natural_key(Usernames[3])
					s = seat.objects.create(position='S', PlayerID=W, TableID=t)
					s.save()
					S = SessionStore()
					S['bmbc'] = request.session['BMBC']
					S['state'] = '1'	## 線上隨機模式
					S['T_id'] = t.pk
					S.create()
				else:
					message = "短時間內創建過多次牌局"
			return render(request,"Member/General.html",locals())
	#if request.POST['BridgeMasterBaseCode'] =="1":
	BMBC = request.POST['BridgeMasterBaseCode']
	request.session['BMBC'] = BMBC
	return render(request, "Member/playmode.html", locals())
#	return redirect("/Member/index/")


def timefilter(t,tabs):
	start = date.today()+timedelta(days=1)
	end = start-timedelta(days=int(t))
	print(end)
	return tabs.filter(time__range=[end,start])

@login_required(login_url='/Member/login/')
def tableinformation(request,tid='x'):
	permission = False
	seats = seat.objects.filter(PlayerID=request.user.id)
	mytable = []
	for s in seats:
		mytable.append(s.TableID.pk)
	mytable = set(mytable)		#去除重複
	tables = table.objects.filter(pk__in=mytable)		#一般使用者
	if request.user.is_staff==True:
		permission = True			#管理者
		tables = table.objects.all()
	name = Name(request)
	if	tid=="x":		# 牌桌資訊一覽
		if request.method=="POST":
			time = request.POST['TimeRange']	#選擇條件
			tables = timefilter(time,tables)
			if  request.POST['BMBC']!="":
				tables = tables.filter(MachineID=request.POST['BMBC'])
			#if request.POST['Mypoint']!="":
			#	#先判斷使用者坐在哪一個位置
			#	Myseat = seat.objects.filter()
				#Mypoint = tables.filter()
			if request.POST['Friend']!="":
				try:
					friend = User.objects.get_by_natural_key(request.POST['Friend'])
				except:
					message = "查無該使用者"
					paginator = Paginator(tables, 5)
					page = request.GET.get('page', '1')
					tables = paginator.page(page)
					return render(request, "Member/table.html", locals())
				seats = seat.objects.filter(PlayerID=friend)
				tid = Q()
				tid.connector = 'OR'		#用 tid1 | tid2 | tid3 |....的方式搜索
				for s in seats:
					s = s.TableID.pk
					tid.children.append(('pk',s))
				tables = tables.filter(tid)
			if 'order' in request.POST:
				ord = request.POST['order']		#排序條件
				tables = tables.order_by(ord)
				if "ORDER" in request.session:
					tables = tables.reverse()
					del request.session["ORDER"]
				else:
					request.session["ORDER"] = '1'
			paginator = Paginator(tables, 5)
			page = request.GET.get('page', '1')
			tables = paginator.page(page)
			return render(request, "Member/table.html",locals())
		paginator = Paginator(tables, 5)
		page = request.GET.get('page','1')
		tables = paginator.page(page)
		return render(request,"Member/table.html",locals())
	#編號.tid 牌桌之牌局資訊一覽
	tables = tables.filter(pk=tid)
	Nseat = seat.objects.filter(TableID=tid,position="N")
	Eseat = seat.objects.filter(TableID=tid, position="E")
	Wseat = seat.objects.filter(TableID=tid, position="W")
	Sseat = seat.objects.filter(TableID=tid, position="S")
	Rounds = rounds.objects.filter(T_id=tid)
	return render(request,"Member/tabledetail.html",locals())

@login_required(login_url='/Member/login/')
def Administrator(request):
	if request.user.is_staff==False:
		message = "你不是管理員"
		return render(request,"Member/index.html",locals())
	name = Name(request)
	users = User.objects.filter(is_staff=False)
	return render(request, "Member/Administrator.html", locals())
@login_required(login_url='/Member/login/')
def usermodify(request,uid='x'):
	if request.user.is_staff==False:
		message = "你不是管理員"
		return render(request,"Member/index.html",locals())
	if uid=='x':
		message = "使用者ID錯誤"
		return render(request,"Member/index.html",locals())
	name = Name(request)
	try:
		user = User.objects.get(id = uid)
	except:
		message = "找不到該使用者"
	return render(request, "Member/usermodify.html", locals())
@login_required(login_url='/Member/login/')
def userdelete(request,uid='x'):
	if request.user.is_staff==False:
		message = "你不是管理員"
		return render(request,"Member/index.html",locals())
	if uid=='x':
		message = "使用者ID錯誤"
		return render(request,"Member/index.html",locals())
	name = Name(request)
	try:
		user = User.objects.get(id = uid)
		user.delete()
		message = "刪除成功"
	except:
		message = "刪除失敗"
	return redirect("/Member/Administrator/")


def cardstring(card):
	Card = card.split('.')
	S = ""
	H = ""
	D = ""
	C = ""
	for c in Card:
		if c[0] == 'S':
			S += c[1]
		elif c[0] == 'H':
			H += c[1]
		elif c[0] == 'D':
			D += c[1]
		elif c[0] == 'C':
			C += c[1]
	Card = S + '.' + H + '.' + D + '.' + C
	return Card
@csrf_exempt
def Json(request):
	if request.body:
		data = json.loads(request.body)		#成功收到pi傳來的資料
		if data['T_id']==None:
			T = None
		else:
			T = table.objects.get(pk=data['T_id'])
			T.RoundNum += 1
			T.save()
		##分成 NESW ##
		Ncard = cardstring(data['N'])
		Ecard = cardstring(data['E'])
		SCard = cardstring(data['S'])
		Wcard = cardstring(data['W'])
		print(Ncard,Ecard,SCard,Wcard)
		#print(data['Date'])
		unit = rounds.objects.create(Event=data['Event'],Site = data['Site'],Date=data['Date'],T_id=T,bid=data['bid'],leader=data['leader'],
									 contract=data['contract'],N=Ncard,E=Ecard,S=SCard,W=Wcard,N_play=data['N'],E_play=data['E'],W_play=data['W'],
									 S_play=data['S'],vulnerable=data['vulnerable'],result=data['result'],
									 declarer=data['declarer'],Rnum=data['Rnum'],score=data['score'])
		unit.save()
	return JsonResponse({'test': 'work!'})
"""
if request.body:
        json_data = json.loads(request.body)
        print(request.body)
        return render(request,"Member/index.html/",locals())
    return render(request,"Member/Json.html/",locals())
    response = HttpResponse(content_type='applicaiton/json')
    tables = table.objects.values()
    response.write("TableInformation:\r\n")
    for t in tables:
        response.write(t)
        response.write("\r\n")
    seats = seat.objects.values()
    response.write("SeatInformation:\r\n")
    for s in seats:
        response.write(s)
        response.write("\r\n")
    roundss = rounds.objects.values()
    response.write("RoundInformation:\r\n")
    for r in roundss:
        response.write(r)
        response.write("\r\n")
    return response
    #return JsonResponse(t)
    #response = HttpResponse(t,content_type='applicaiton/json')
    #return render(request,"Member/Json.html/",locals())
    """

