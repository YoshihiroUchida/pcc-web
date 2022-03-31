from django.shortcuts import render

def index(request):
    contents = {
        "name" : "Programming",
        "desc" : "準備中…",
    }
    other = {
        "name" : "Other",
        "desc" : "準備中…",
    }
    news = {
        "name" : "News",
        "desc" : "準備中…",
    }

    lst = [contents, other, news]

    params = {
        'title' : 'PCC Office',
        'content_list' : lst,
    }
    return render(request, 'pcc_home/index.html', params)
