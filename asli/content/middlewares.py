from django.urls import path
from typing import Any
from django.shortcuts import render,redirect

FREE_URL =[
    '/accounts/login/',
    '/accounts/singup/',
    '/accounts/veryfy/',
    '/accounts/password_reset/',
    '/accounts/password_reset_done/',
    '/accounts/password_reset_confirm/<uidb64>/<token>/',
    '/accounts/password_Reset_complete/',
    '/content/home/',
    '/content/seryals/',
]


class LoginRequired:
    def __init__(self,get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        if not request.user.is_authenticated and request.path not in FREE_URL:
            return redirect('login')
        
        response = self.get_response(request)
        return response
        