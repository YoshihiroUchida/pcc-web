from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Prog_contents

def Set_contents(n, d, u):
    data = {
        "name" : n, 
        "desc" : d, 
        "url"  : u,
    }
    return data

#--------------------------------------------------
def index(request):
    prog = Set_contents("Programming", "Pythonによるプログラミング", "program")
    other = Set_contents("Other", "準備中", "#")
    news = Set_contents("News", "準備中", "#")

    lst = [prog, other, news]

    params = {
        'title' : 'PCC Office',
        'content_list' : lst,
    }
    return render(request, 'pcc_home/index.html', params)

#--------------------------------------------------
# ログイン後のみ利用可
@login_required
def program(request):
    data = Prog_contents.objects.all()
    params = {
        'title' : 'Programming',
        'tab_list' : data,
    }
    return render(request, 'pcc_home/page1.html', params)