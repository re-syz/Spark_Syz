"""
131072
280918
CS+X




"""


# =============

from django.shortcuts import render, redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import time
from guestbook.models import TextMessage


# =============

def index(request):
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def guestbook(request):
    Kort = "Kort"
    Spark = "Spark"

    # t1 = TextMessage.objects.create(talker=Kort, message="Hey, Spark!")
    # t2 = TextMessage.objects.create(talker=Spark, message="Hello, Kort! :)")

    if request.method == 'POST':
        _talker = request.POST.get('name')
        if request.user.is_authenticated:
            _talker = request.user.username
        _message = request.POST.get('msg')
        TextMessage.objects.create(talker=_talker, message=_message)

    msgs = TextMessage.objects.all()

    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.GET.get('msg_search') is not None:
                msg_search = request.GET.get('msg_search')
                msgs = TextMessage.objects.filter(message__icontains=msg_search)

    return render(request, 'guestbook.html', locals())


def base(request):

    return render(request, 'base.html', locals())
