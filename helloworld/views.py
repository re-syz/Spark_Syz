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
import random
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

    if 'name' in request.GET:
        txt_msg = TextMessage.objects.create(talker=request.GET['name'], message=request.GET['msg'])

    # t1 = TextMessage.objects.create(talker=Kort, message="Hey, Spark!")
    # t2 = TextMessage.objects.create(talker=Spark, message="Hello, Kort! :)")

    msgs = TextMessage.objects.all()

    return render(request, 'guestbook.html', locals())

def base(request):

    return render(request, 'base.html', locals())
