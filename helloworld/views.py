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
from django import template
from django.contrib.auth.models import Group
import time
from guestbook.models import TextMessage


# =============

def index(request):
    return render(request, 'index.html', locals())


def base(request):
    return render(request, 'base.html', locals())


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

    users_in_group = Group.objects.get(name="TextMessage").user_set.all()

    if request.user.is_authenticated:
        current_user = request.user
        if current_user not in users_in_group:
            my_group = Group.objects.get(name='TextMessage')
            my_group.user_set.add(current_user)

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


def personal_history(request):
    if request.user.is_authenticated:
        user = request.user
        msgs = TextMessage.objects.filter(talker__exact=user)

    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.GET.get('msg_search') is not None:
                msg_search = request.GET.get('msg_search')
                msgs = TextMessage.objects.filter(message__icontains=msg_search)

    return render(request, 'personal_history.html', locals())
