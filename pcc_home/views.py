from django.shortcuts import render

def index(request):
    params = {
        'title' : 'PCC Office',
    }
    return render(request, 'pcc_home/index.html', params)
