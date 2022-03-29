from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

# ログイン用のクラス
class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

# ログアウト用のクラス
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'pcc_home/index.html'