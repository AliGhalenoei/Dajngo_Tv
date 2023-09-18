from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('singup/',views.SingupView.as_view(),name='singup'),
    path('veryfy/',views.VeryfySingupView.as_view(),name='veryfy'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('password_reset/',views.UserPasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',views.UserPasswordResetDone.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',views.UserPasswordResetConfirm.as_view(),name='password_reset_confirm'),
    path('password_Reset_complete/',views.UserPasswordResetComplete.as_view(),name='password_reset_complete'),
]
