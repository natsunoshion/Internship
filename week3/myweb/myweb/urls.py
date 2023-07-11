"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from learn.views import index   # 引入视图函数
from learn.views import index, User, UserDetails, login

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),            # 新增路由映射
    # #path('hw', index),          # 新增路由映射，换个映射url地址
    # path('user', User),            # 新增路由与对应的视图函数生成新的接口
    # path('login', login),
    path('learn/', include('learn.urls')),
]
