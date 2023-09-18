from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from extensions.utils import time_jalali
# Create your models here.

class User(AbstractBaseUser):
    phone=models.CharField(max_length=11,unique=True)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=('email',)

    objects=UserManager()

    def __str__(self) -> str:
        return self.phone
    
    def time_persian(self):
        return time_jalali(self.publish)

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
class OTP(models.Model):
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()

    def __str__(self) -> str:
        return f'{self.phone} Code Feryfy... {self.code}'
    
    



