from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    '''用户映射类，已经继承了 AbstractUser，它已经包含了一些基本的字段，如用户名和密码
    '''

    pass

class UserDetails(models.Model):
    '''用户详细信息映射类，包括电话、邮箱等属性
    '''

    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
