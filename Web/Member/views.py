from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
# superuser admin/admin123		
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
    if request.user.is_authenticated:
        name=request.user.first_name
        message="登入成功"
        return render(request, "Member/index.html", locals())
    else:		
        return redirect("/Member/login/")

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
	if not request.user.is_authenticated:		#確認登入狀態
		return redirect("/Member/login/")
	user=request.user
	username=user.username
	name=user.first_name
	if request.method == 'POST':
		new_name= request.POST['firstname']
		cur_pass= request.POST['current_pass']
		new_pass= request.POST['new_pass']
		check_pass= request.POST['check_pass']
		if (not cur_pass=="") or (not new_pass==""): 	#是否修改密碼
			if not user.check_password(cur_pass):					
				message="當前密碼錯誤"
				return render(request,"Member/modify.html",locals())
			if new_pass!=check_pass:
				message="新密碼不符"
				return render(request,"Member/modify.html",locals())
			user.set_password(new_pass)	
		if new_name is not None:
			user.first_name=new_name
		user.save()
		if (not cur_pass=="") or (not new_pass==""): 	#是否修改密碼
			User = authenticate(username=username, password=new_pass)	#直接重新登入
			auth.login(request,User)
		return redirect("/Member/index/")
	return render(request,"Member/modify.html",locals())
