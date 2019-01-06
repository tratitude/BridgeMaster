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
from dwebsocket.decorators import accept_websocket,require_websocket
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse
import time,json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date,timedelta
from django.db.models	 import Q


# Create your views here.
# superuser admin/admin123
def State(request):
	StateList = []
	SessionStore.clear_expired()
	sessions = Session.objects.all()
	for session in sessions:
		s = session.get_decoded()
		if 'BMBC' in s and 'state' in s:
			StateList.append({s['BMBC']:s['state']})
	return HttpResponse(StateList)

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
			message = '登入失敗！'
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
	auth.logout(request)
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
def playmode(request,pm='x'):
	name = Name(request)
	if pm!='x':
		if(pm==0):	#Classic
			ClassicGames = rounds.objects.filter(T_id=None,Rnum=0)
			return render(request,"Member/Classic.html",locals())
		elif (pm==1):	#General
			Users = []
			SessionStore.clear_expired()
			sessions = Session.objects.all()
			try:
				for session in sessions:
					s = session.get_decoded()
					if s['BMBC']==request.session['BMBC']:		#取出所有BMBC相同的玩家
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
				request.session['state']=1			#發送到指定BMBC主機
				# 禁止短時間內多次創建同主機下的Table
				if	table.objects.filter(MachineID=request.session['BMBC'],time__range=[datetime.now()-timedelta(minutes=10),datetime.now()])==None:
					t = table.objects.create(MachineID=request.session['BMBC'],NS_TotalPoint=0,EW_TotalPoint=0,RoundNum=0)
					t.save()
					s = seat.objects.create(position='N',PlayerID=Usernames[0],TableID=t)
					s.save()
					s = seat.objects.create(position='E', PlayerID=Usernames[1], TableID=t)
					s.save()
					s = seat.objects.create(position='W', PlayerID=Usernames[2], TableID=t)
					s.save()
					s = seat.objects.create(position='S', PlayerID=Usernames[3], TableID=t)
					s.save()
				message = "遊戲準備開始!!!"
			return render(request,"Member/General.html",locals())
	#if request.POST['BridgeMasterBaseCode'] =="1":
	BMBC = request.POST['BridgeMasterBaseCode']
	request.session['BMBC'] = BMBC
	request.session['state'] = 1
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
			if request.POST['Friend']!="":
				try:
					friend = User.objects.get_by_natural_key(request.POST['Friend'])
				except:
					message = "查無該使用者"
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
			return render(request, "Member/table.html", locals())
		return render(request,"Member/table.html",locals())
	#編號.tid 牌桌之牌局資訊一覽
	tables = tables.filter(pk=tid)
	Nseat = seat.objects.filter(TableID=tid,position="N")
	Eseat = seat.objects.filter(TableID=tid, position="E")
	Wseat = seat.objects.filter(TableID=tid, position="W")
	Sseat = seat.objects.filter(TableID=tid, position="S")
	Rounds = rounds.objects.filter(T_id=tid)
	return render(request,"Member/tabledetail.html",locals())


def Administrator(request):

	return render(request, "Member/Administrator.html", locals())
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
		#print(data['Date'])
		unit = rounds.objects.create(Event=data['Event'],Site = data['Site'],Date=data['Date'],T_id=T,bid=data['bid'],leader=data['leader'],
									 contract=data['contract'],N=data['N'],E=data['E'],W=data['W'],
									 S=data['S'],vulnerable=data['vulnerable'],result=data['result'],
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

