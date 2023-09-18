from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserCreationForm(forms.ModelForm):
    password=forms.CharField()
    password2=forms.CharField()

    class Meta:
        model=User
        fields=('phone','email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            raise ValidationError('Passwords is not match...')
        return cd['password2']
    
    def save(self, commit: bool = True) -> Any:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model=User
        fields=('phone','email')

class VeryfySingupForm(forms.Form):
    code = forms.IntegerField()
        


    