from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse('ojbk')

def login(request):
    return redirect('/index')
