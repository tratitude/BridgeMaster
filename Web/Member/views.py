from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
		
def login(request):
	if request.user.is_authenticated:		#確認登入狀態
		return redirect("/Member/index/")
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect("/Member/index/")			
			else:
				message = '帳號尚未啟用！'
				return render(request, "Member/login.html", locals())
		else:
			message = '登入失敗！'
	return render(request, "Member/login.html", locals())

def index(request):
    if request.user.is_authenticated:
        name=request.user.first_name
        message="登入成功"
        return render(request, "index.html", locals())
    else:		
        return redirect("/login/")


