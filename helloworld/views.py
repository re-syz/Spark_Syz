"""
131072
280918
CS+X
"""






# =============

from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random



# =============

def index(request):
    Kort = "Kort"
    Spark = "Spark"
    default_msg = "Hey! Here are random photos on the Internet."
    msgs = [default_msg for i in range(len(default_msg))]
    imgids = [random.randint(1, 500) for i in range(len(default_msg))]
    imgurls = ["https://picsum.photos/200/200/?image={}".format(imgid) for imgid in imgids]
    return render(request, 'index.html')
