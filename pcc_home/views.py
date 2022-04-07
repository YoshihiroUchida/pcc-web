from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import PG_contents, Home_contents
from .forms import PG_Edit_form, PG_Reg_form

#==================================================
# Home画面の表示
def index(request):
    # 管理者の場合
    if (request.user.is_superuser):
        data = Home_contents.objects.all()
    else:
        data = Home_contents.objects.filter(auth = False) # 権限が必要ないものだけ取得

    params = {
        'title' : 'PCC Office',
        'content_list' : data,
    }
    return render(request, 'pcc_home/index.html', params)

#==================================================
# プログラミング教材のアップロード
@login_required
def setting(request):
    # 送信時の処理
    if (request.method == 'POST'):
        post_object = PG_contents() # モデルのインスタンス
        content = PG_Edit_form(request.POST, instance = post_object)
        content.save()
        return redirect(to = '/home/program') # スライド画面へ

    params = {
        'form' : PG_Reg_form(),
    }
    return render(request, 'pcc_home/setting.html', params)

#==================================================
# コンテンツの編集
@login_required
def edit(request, num):
    edit_object = PG_contents.objects.get(id = num)
    if (request.method == 'POST'):
        content = PG_Edit_form(request.POST, instance = edit_object)
        content.save()
        return redirect(to = '/home/program')

    params = {
        'id' : num,
        'form' : PG_Edit_form(instance = edit_object)
    }
    return render(request, 'pcc_home/edit.html', params)

#==================================================
# プログラミング教材の表示
@login_required
def program(request):
    data = PG_contents.objects.all().order_by('num')
    params = {
        'title' : 'Programming',
        'tab_list' : data,
    }
    return render(request, 'pcc_home/page1.html', params)

#==================================================
# ニュースの表示
@login_required
def news(request):
    return render(request, 'pcc_home/news.html', {})
