from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# 引入所需映射类
from .models import User, UserDetails

# Create your views here.
def index(request):
    return HttpResponse('Hello World.')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # 设置 Cookie，30 秒后即失效
            response = redirect('../welcome')
            response.set_cookie('username', username, max_age=30, path='/learn')
            response.set_cookie('password', password, max_age=30, path='/learn')
            return response
        else:
            error_message = 'Invalid username or password.'
    elif request.method == 'GET':
        # 使用 Cookie 进行自动登录
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('../welcome')
        else:
            error_message = 'Automatic login failed. Please log in manually.'
    return render(request, 'learn/login.html', {'error_message': error_message})

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']
        
        # 创建User实例
        user = User.objects.create_user(username=username, password=password)
        
        # 创建UserDetails实例
        user_details = UserDetails(phone=phone, email=email, user=user)
        user_details.save()
        
        return redirect('../login')  # 注册成功后跳转到登录页面

    return render(request, 'learn/register.html')

@login_required
def welcome(request):
    # 获取当前登录用户对象
    user = request.user

    # 获取所有用户的详细信息
    users = User.objects.all()

    return render(request, 'learn/welcome.html', {'users': users})
