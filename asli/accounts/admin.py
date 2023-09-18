from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUSerAdmin
from django.contrib.auth.models import Group
from .models import *
from .forms import *

# Register your models here.

class UserAdmin(BaseUSerAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=('phone','email','is_admin','time_persian')
    list_filter=('is_active','is_admin')
    search_fields=('email',)
    filter_horizontal=()
    ordering=('email','phone')

    fieldsets=(
        (None,{'fields':('phone','email','password')}),
        ('Status',{'fields':('is_active','is_admin')}),
        ('Time',{'fields':('publish','last_login')}),
    )

    add_fieldsets=(
        (None,{'fields':('phone','email','password','password2')}),
    )

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)

admin.site.register(OTP)

