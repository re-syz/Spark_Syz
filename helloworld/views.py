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
    return render(request, 'guestbook.html')
