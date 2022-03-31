from django.shortcuts import render

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
def program(request):
    return render(request, 'pcc_home/page1.html')