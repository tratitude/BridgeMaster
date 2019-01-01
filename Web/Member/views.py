from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django .utils import timezone
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.sessions.models import Session
from django.views import View
from Member.models import rounds,table,seat
from django.contrib.auth.decorators import login_required
from dwebsocket import accept_websocket
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse
import time
from datetime import datetime



# Create your views here.
# superuser admin/admin123
@accept_websocket
def connect(request):
	if request.is_websocket():
		print(1213312131231)
		message = request.websocket.wait()  # 接受前段发送来的数据
		print(message)
		while 1:
			if message:
				request.websocket.send('test')  # 发送给前段的数据
				print(message)
				time.sleep(2)
			elif message=="88888":
				print(232222222222)
				request.websocket.colse()


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
		if	 str(user.id) in logged_in:
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
			return render(request,"Member/Classic.html",locals())
		elif (pm==1):	#General
			BMBCs = []
			SessionStore.clear_expired()
			sessions = Session.objects.all()
			for session in sessions:
				s = session.get_decoded()
				BMBCs.append(s)
			return render(request,"Member/General.html",locals())
	#if request.POST['BridgeMasterBaseCode'] =="1":
	BMBC = request.POST['BridgeMasterBaseCode']
	request.session['BMBC'] = BMBC
	return render(request, "Member/playmode.html", locals())
#	return redirect("/Member/index/")


@login_required(login_url='/Member/login/')
def tableinformation(request,tid='x'):
	name = Name(request)
	if	tid=="x":
		tables = table.objects.all()
		return render(request,"Member/table.html",locals())
	tables = table.objects.filter(pk=tid)
	Nseat = seat.objects.filter(TableID=tid,position="N")
	Eseat = seat.objects.filter(TableID=tid, position="E")
	Wseat = seat.objects.filter(TableID=tid, position="W")
	Sseat = seat.objects.filter(TableID=tid, position="S")
	Rounds = rounds.objects.filter(T_id=tid)
	return render(request,"Member/tabledetail.html",locals())

