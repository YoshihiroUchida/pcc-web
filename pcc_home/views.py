from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Prog_contents
from .forms import Prog_contents_form, Prog_form

def Set_contents(n, d, u):
    data = {
        "name" : n, 
        "desc" : d, 
        "url"  : u,
    }
    return data

#--------------------------------------------------
# Home画面の表示
def index(request):
    lst = []
    lst.append(Set_contents("Programming", "Pythonによるプログラミング", "program"))
    lst.append(Set_contents("Other", "準備中", "#"))
    lst.append(Set_contents("News", "準備中", "#"))
    # 管理者のみ「設定」を選択可
    if (request.user.is_superuser):
        lst.append(Set_contents("Setting", "教材の追加", "setting"))

    params = {
        'title' : 'PCC Office',
        'content_list' : lst,
    }
    return render(request, 'pcc_home/index.html', params)

#--------------------------------------------------
# プログラミング教材のアップロード
@login_required
def setting(request):
    # 送信時の処理
    if (request.method == 'POST'):
        post_object = Prog_contents() # モデルのインスタンス
        content = Prog_contents_form(request.POST, instance = post_object)
        content.save()
        return redirect(to = '/home/program') # スライド画面へ

    params = {
        'form' : Prog_form(),
    }
    return render(request, 'pcc_home/setting.html', params)

#--------------------------------------------------
# コンテンツの編集
@login_required
def edit(request, num):
    edit_object = Prog_contents.objects.get(id = num)
    if (request.method == 'POST'):
        content = Prog_contents_form(request.POST, instance = edit_object)
        content.save()
        return redirect(to = '/home/program')

    params = {
        'id' : num,
        'form' : Prog_contents_form(instance = edit_object)
    }
    return render(request, 'pcc_home/edit.html', params)

#--------------------------------------------------
# プログラミング教材の表示
@login_required
def program(request):
    data = Prog_contents.objects.all().order_by('num')
    params = {
        'title' : 'Programming',
        'tab_list' : data,
    }
    return render(request, 'pcc_home/page1.html', params)