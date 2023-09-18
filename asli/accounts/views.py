from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import views as auth_view
from django.contrib.auth import login,logout,authenticate
import random
from utils import send_otp
from .models import *
from .forms import *

# Create your views here.

class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        try:
            phone = request.POST.get('phone')
            password = request.POST.get('password')        
            user = authenticate(phone = phone , password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
        except:
            return redirect('login')
        
class SingupView(View):
    template_name = 'accounts/singup.html'

    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        try:
            User.objects.get(phone = phone)
            print('=========Phone is alredy===========')
            return redirect('singup')
        except:
            pass

        try:
            User.objects.get(email = email)
            print('=========email is alredy===========')
            return redirect('singup')
        except:
            pass

        try:
            if password != password2:
                print('==========Passwords is Not match==========')
                return redirect('singup')                
        except:
            pass

        random_code = random.randint(1000,9999)
        send_otp(phone , random_code)
        OTP.objects.create(
            phone = phone,
            code = random_code
        )
        request.session['singup_info'] = {
            'phone':phone,
            'email':email,
            'password':password,
        }
        return redirect('veryfy')


class VeryfySingupView(View):
    template_name = 'accounts/veryfy.html'
    form_class = VeryfySingupForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    # def post(self,request):
    #     try:
    #         user_session = request.session['singup_info']  
    #         get_phone = OTP.objects.get(phone = user_session['phone'])
    #         code = request.POST.get('code')
    #         if code == get_phone.code:
    #             User.objects.cretae_user(
    #                 phone=user_session['phone'],
    #                 email=user_session['email'],
    #                 password=user_session['password'],
    #             )
    #             get_phone.delete()
    #             return redirect('login')
    #         else:
    #             redirect('veryfy')
    #     except :
    #         pass

    def post(self,request):
        user_session = request.session['singup_info']  
        get_phone = OTP.objects.get(phone = user_session['phone'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == get_phone.code:
                User.objects.cretae_user(
                    phone=user_session['phone'],
                    email=user_session['email'],
                    password=user_session['password'],
                  )
                get_phone.delete()
                return redirect('login')
            else:
                 redirect('veryfy')
        return render(request,self.template_name,{'form':form})



class LogoutView(View):

    def get(self,request):
        logout(request)
        return redirect('login')
    
class UserPasswordResetView(auth_view.PasswordResetView):
    template_name='accounts/password_reset_form.html'
    success_url=reverse_lazy('password_reset_done')
    email_template_name='accounts/password_reset_email.html'

class UserPasswordResetDone(auth_view.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

class UserPasswordResetConfirm(auth_view.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    success_url=reverse_lazy('password_reset_complete')

class UserPasswordResetComplete(auth_view.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'
        
