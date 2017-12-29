import datetime

from django.shortcuts import render
from django.http import HttpResponse
from money.models import user
from datetime import datetime

# Create your views here.

def home(request):
    str='hhhooo'
    return HttpResponse(str)

def detail(request, my_args):
    player_id=user.objects.all()[int(my_args)]
    str="查询用户ID: {:10}   用户昵称: {}".format(player_id.pid,player_id.nick)
    return HttpResponse(str)

def test(request):
    player=user.objects.all()
    return render(request,'test.html',{'player':player})