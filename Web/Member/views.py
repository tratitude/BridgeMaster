from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.views import View
from Member.models import rounds,table,seat



# Create your views here.
# superuser admin/admin123
def verify(request):
	if not request.user.is_authenticated:  # 確認登入狀態
		return redirect("/Member/login/")
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
		if user is not None:
				auth.login(request,user)
				return redirect("/Member/index/")
		else:
			message = '登入失敗！'
	return render(request, "Member/login.html", locals())

def index(request):
	name = verify(request)
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
	return redirect('/Member/login/')
	message="登出成功"	

def modify(request):
	verify(request)
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

def playmode(request,pm='x'):
	name = verify(request)
	if pm!='x':
		if(pm==0):	#Classic
			return render(request,"Member/Classic.html",locals())
		elif (pm==1):	#General
			return render(request,"Member/General.html",locals())
	if request.POST['BridgeMasterBaseCode'] =="1":
		request.session['BMBC'] = request.POST['BridgeMasterBaseCode']
		return render(request, "Member/playmode.html", locals())
	return redirect("/Member/index/")

def tableinformation(request,tid='x'):
	name = verify(request)
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

