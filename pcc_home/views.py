from django.shortcuts import render

def index(request):
    params = {
        'title' : 'PCC HP',
    }
    return render(request, 'pcc_home/index.html', params)
