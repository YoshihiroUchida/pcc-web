from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def Set_contents(n, d, u):
    data = {
        "name" : n, 
        "desc" : d, 
        "url"  : u,
    }
    return data

#--------------------------------------------------
def Set_pgm_contents(num, title, url):
    data = {
        'number' : str(num),
        'sub_title' : title,
        'url' : url,
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
    lst = []
    lst.append(Set_pgm_contents(1, "プログラミングとは?", "https://docs.google.com/presentation/d/e/2PACX-1vRCR6-FsFsvyewZcUw4tPBNpJZHFe-cjHWEky_2rCbmETFsrGcdU6r1h32XmcvSf_ttckcMjjh-tPuu/embed?start=false&loop=false&delayms=3000"))
    lst.append(Set_pgm_contents(2, "Spyderのつかいかた", "https://docs.google.com/presentation/d/e/2PACX-1vRWiINR95pAuelWGSUt4NKkI7ZIZOH9wQtHy19llGSNDvep3vZAmwfmO6aLn-TuCCzP-Xwo3iu_PCxF/embed?start=false&loop=false&delayms=3000"))
    lst.append(Set_pgm_contents(3, "変数のつかいかた", "https://docs.google.com/presentation/d/e/2PACX-1vShsE3EHzSRo-Pm5Ezc_Y7V9tRA47_RovfLp9M-Jet4c4csoUjJrUh0ONUJMyh82OQETANqAIUrAdrc/embed?start=false&loop=false&delayms=3000"))
    
    params = {
        'title' : 'Programming',
        'tab_list' : lst,
    }
    return render(request, 'pcc_home/page1.html', params)